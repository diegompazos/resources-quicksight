import boto3
import json
import pandas as pd
import argparse
from list_account_dashboards import list_account_dashboards
from list_account_analysis import list_account_analysis
from list_account_datasets import list_account_datasets
from list_account_datasources import list_account_datasources
from dict_to_dataframe import dict_to_df
from date_time import date_time_file

parser = argparse.ArgumentParser()
parser.add_argument("-method", help="Desired boto3 Method.")
parser.add_argument("-account_id", help="Account ID of AWS Account.", type=str)
parser.add_argument("-aws_region", help="Desired AWS region.", type=str)
args = parser.parse_args()

namespace = 'default'

session = boto3.Session(profile_name = 'default')
qs_client = session.client('quicksight')

def list_and_save(method):
    df = dict_to_df(getattr(qs_client, method)(args.account_id, args.aws_region, namespace), f'{method} ')
    df.to_csv(f'reports/list-{method}-{date_time_file()}.csv', encoding = 'utf-8-sig')

list_and_save(args.method)