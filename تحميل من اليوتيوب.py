from pytube import YouTube

link = input('hi inter link youtube:')#رابط التحميل
yt = YouTube(link)
videos = yt.streams.filter(subtype='mp4').all()#طباعه الصيغ المتوفره
i = 1
for stream in videos:
    print(str(i) + " - " + str(stream))
    i += 1
stream_number = int(input("Enter number :"))#اختيار الصيغه
video = videos[stream_number - 1]
video.download("")#راح يتحمل بالمجلد الي فيه ملف البايثون
print("done")


input("enter:")
# اتمني انكم استفدتو منه