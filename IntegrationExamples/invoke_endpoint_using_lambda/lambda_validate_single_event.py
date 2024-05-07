from lambda_function import lambda_handler

event = {
     "instances": [
         {
             "features": ["2012-12-19 17:00:00",4,0,1,1,16.4,20.455,50,26.0027]
             
         }
    ]
}

res = lambda_handler(event,None)

print(res)