# aws-cloudwatch-logs-lambda
The sample cloudwatch.json and lambdaTest.json are for SMS Failure

## Manually publish logstream
Edit the sample/sms-failure-budgetlimit.json timestamp to current epoch timestamp (take note, the epoch is in long format, add 000 behind the timestamp if you were to get current epoch time from: https://www.epochconverter.com/)

Go to cloudwatch logGroup, create a new logstream name "sample"

CLI Command:
```
aws logs put-log-events --log-group-name <logGroupName> --log-stream-name sample --log-events file://sample/sms-failure-budgetlimit.json
```
You might need to provide --sequence-token to the cli above if you want to publish subsequence logs

## Create Lambda Functions
environment: python3.8
Code sample: lambda/processFailSMS.py

## Create Subscription
Go to LogGroup Stream add the following to filter metric
```
{$.status=FAILURE}
```
