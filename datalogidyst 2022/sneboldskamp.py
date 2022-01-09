w,h,s = list(map(int, input().split()))

snowVolume = w * h * s

remainder = snowVolume % 500
snowballs = (snowVolume - remainder) / 500

print(int(snowballs))

if snowVolume % 500 >= 200:
    print("ja")
else:
    print("nej")


