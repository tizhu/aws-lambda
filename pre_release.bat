zip -j deploy.zip lambda_function.py
aws lambda update-function-code --function-name process_s3_data_function --zip-file=fileb://deploy.zip
aws lambda update-function-configuration --function-name process_s3_data_function  --environment 'Variables={env=dev}'
aws lambda invoke --function-name process_s3_data_function --invocation-type RequestResponse --payload fileb://events/input_event.json response_output.json