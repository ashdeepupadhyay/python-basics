monthConversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sept":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(monthConversions['Mar'])
print(monthConversions.get('Dec'))
print(monthConversions.get('lec','Not a valid key'))

