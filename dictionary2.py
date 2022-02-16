# list of dictionaries

colors = [
   {
     "colors": "red",
     "values": "#f00"
   },
   {
     "colors": "green",
     "values": "#0f0"
   },
   {
     "colors": "yellow",
     "values": "#ff0"
   },
   {
     "colors": "black",
     "values": "#000"
     }
]


for val in range(0,len(colors)):
    print(colors[val]['colors'])
    print(colors[val]['values'])



for item in colors:
    print(item['colors'] , item['values'])
    
