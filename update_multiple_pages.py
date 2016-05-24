import add_page
import urllib
from concurrent import futures

urls = [ 'TinaTheMalinois',
         'Netanyahu',
         'NaftaliBennett'
         'Israeli-Kennel-Club-ההתאחדות-הישראלית-לכלבנות-827972747231428',
         'ayelet.benshaul.shaked',
         'sharren1',
         'MFeiglin',
         'georgewbush',
         'DonaldTrump',
         'berniesanders',
         'mexicanswithguns',
         'StandWithUs',
         'Einsturzende-Neubauten',
         'primusville',
         ]

with futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
    for url in urls:
        executor.submit(add_page.update_page_by_name, url)