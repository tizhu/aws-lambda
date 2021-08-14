zip -j deploy.zip lambda_function.py
aws lambda update-function-code --function-name process_s3_data_function --zip-file=fileb://deploy.zip
aws lambda update-function-configuration --function-name process_s3_data_function  --environment 'Variables={env=dev}'
aws lambda invoke --function-name process_s3_data_function --invocation-type Event --payload fileb://events/inputFile.txt