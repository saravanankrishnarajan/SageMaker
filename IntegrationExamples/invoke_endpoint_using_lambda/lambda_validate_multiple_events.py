from lambda_function import lambda_handler

event = {
     "instances": [
         {
             "features": ["2012-12-19 17:00:00",4,0,1,1,16.4,20.455,50,26.0027]
             
         },
         {
             "features": ["2012-12-19 18:00:00",4,0,1,1,15.58,19.695,50,23.9994]
         },
         {
             "features": ["2012-12-10 01:00:00",4,0,1,2,14.76,18.94,100,0]
         }
    ]
}

res = lambda_handler(event,None)

print(res)