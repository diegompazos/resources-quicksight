# List AWS QuickSight Resources

_Simple way of listing quicksight resources of an AWS account._

### Why 

During early stages of QuickSight, there was not a friendly and low code way of listing the resources created by users at QuickSight.

---

### What

Simple methods were created to retrieve the resources. With these methods, you can create CSV files to send to others responsible for the account without using the AWS CloudShell.

---

### How

Choose one or various methods such as:

``` list_account_analysis ``` <br>
``` list_account_dashboards ``` <br>
``` list_account_datasets ``` <br>
``` list_account_datasources ``` <br>

Set your credentials and configs:

``` AWS account id ``` <br>
``` AWS region ```

_Methods are going to use boto3 (Python SDK). You need to authenticate your credentials or use a notebook with IAM permissions to access the AWS QuickSight API._


