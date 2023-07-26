def list_account_datasets(qs_client, account_id, aws_region):
    
    response_dataset = qs_client.list_data_sets(AwsAccountId = account_id, MaxResults = 100)
    results_dataset = response_dataset['DataSetSummaries']

    while "NextToken" in response_dataset:
        response_dataset = qs_client.list_data_sets(
            AwsAccountId = account_id,
            MaxResults = 100,
            NextToken=response_dataset["NextToken"]
        )
        results_dataset.extend(response_dataset["DataSetSummaries"])
        
    return dict(zip([x.get('Name') for x in results_dataset], [x.get('DataSetId') for x in results_dataset]))