# libraries

import argparse
import pandas as pd
import requests
import numpy as np
import os
from shapely.geometry import Point
import geopandas as gpd   
import sys



# Script functions 


# Argument parser function

parser = argparse.ArgumentParser()
parser.add_argument( "--tipo", dest = "tipo", default = "CloserStation", 
help = "parametro para selecionar el tipo de ejecucion. Posibles valores: MasCercana , TodasEstaciones"
)
args = parser.parse_args(sys.argv[1:])





def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

def distance_meters(start, final):
    # return the distance in metres between to latitude/longitude pair point in degrees 
    return start.distance(final)

def datasets():
    templos_catolicos = requests.get('https://datos.madrid.es/egob/catalogo/209426-0-templos-catolicas.json')
    templos_catolicos = templos_catolicos.json()
    templos_catolicos = pd.json_normalize(templos_catolicos['@graph'])
    
    templos_no_catolicos = requests.get('https://datos.madrid.es/egob/catalogo/209434-0-templos-otros.json')
    templos_no_catolicos = templos_no_catolicos.json()
    templos_no_catolicos = pd.json_normalize(templos_no_catolicos['@graph'])
    
    
    templos_catolicos = templos_catolicos.drop(['@id', '@type', 'id', 'relation', 'address.district.@id', 'address.area.@id', 'address.postal-code', 'organization.organization-desc', 'organization.accesibility', 'organization.schedule', 'organization.services', 'organization.organization-name'], axis=1)
    templos_catolicos = templos_catolicos.rename(columns={'title':'Place of interest', 'address.locality':'City', 'address.street-address':'Place address', 'location.latitude':'lat_start', 'location.longitude':'long_start'})
    templos_catolicos ['Type of place'] = 'catolicas'
    
    templos_no_catolicos = templos_no_catolicos.drop(['@id', '@type', 'id', 'relation', 'address.district.@id', 'address.area.@id', 'address.postal-code', 'organization.organization-desc', 'organization.accesibility', 'organization.schedule', 'organization.services', 'organization.organization-name'], axis=1)
    templos_no_catolicos = templos_no_catolicos.rename(columns={'title':'Place of interest', 'address.locality':'City', 'address.street-address':'Place address', 'location.latitude':'lat_start', 'location.longitude':'long_start'})
    templos_no_catolicos["Type of place"] = "no_catolicas"
    
    frames = [templos_catolicos, templos_no_catolicos]
    df_origen = pd.concat(frames)
    df_origen ['start'] = df_origen.apply(lambda x: to_mercator(x['lat_start'], x['long_start']), axis =1)
    return df_origen

def df_bicimad():
    df_bicimad = pd.read_json("data/bicimad_stations.json")
    df_bicimad ['LATITUD'] = [float(index.split(',')[1].replace("]", "")) for index in df_bicimad['geometry_coordinates']]
    df_bicimad ['LONGITUD'] = [float(index.split(',')[0].replace("[", "")) for index in df_bicimad['geometry_coordinates']]
    df_bicimad = df_bicimad.drop(['id', 'light', 'number', 'activate', 'no_available', 'total_bases', 'dock_bikes', 'free_bases', 'reservations_count', 'geometry_type'], axis=1)
    df_bicimad = df_bicimad.rename(columns={'name': 'BiciMAD station', 'address': 'Station location', 'LONGITUD':'long_finish', 'LATITUD':'lat_finish'})
    df_bicimad ['final'] = df_bicimad.apply(lambda x: to_mercator(x['lat_finish'], x['long_finish']), axis =1)
    return df_bicimad

def merge():
    df_merge = datasets().merge(df_bicimad(), how = 'cross')
    df_merge ['Distance'] = df_merge.apply(lambda x: distance_meters(x['final'], x['start']), axis =1)
    return df_merge

def min_distance():
    x = str(input('Enter the Place of Interest: '))
    y = merge()[merge()['Place of interest']== x]
    return y.sort_values(by='Distance', ascending=True).head(1).drop(['City', 'lat_start', 'long_start', 'start', 'geometry_coordinates', 'long_finish', 'lat_finish', 'final'], axis = 1)


def all_min_stations():
    return merge().sort_values(by = "Distance", ascending = True).groupby('Place of interest')['Type of place','Place address','BiciMAD station', 'Station location','Distance'].nth(0).drop(["Distance"], axis = "columns")

print('\n')
print('\n')
print('--- Hi everyone!! ---')
print('\n')
print('\n')

if args.tipo == "CloserStation":
    ubicacion_mas_cercana = min_distance()
    # print(ubicacion_mas_cercana)
    ubicacion_mas_cercana.to_csv("data/closer_station.csv", sep= ";")
    print("Closest station in a CSV file")
elif args.tipo == "AllStations":
    distancias_ubicacion = all_min_stations()
    # print(distancias_ubicacion)
    distancias_ubicacion.to_csv("data/all_locations.csv", sep= ";")
    print("All stations in a CSV file")
else:
    print("Wrong option, you can only print CloserStation or AllStations")