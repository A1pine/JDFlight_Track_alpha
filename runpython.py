

runsum = 0

while True:
    runsum+=1
    print("第%s次运行结果:"%(runsum))
    from SingleFlightTrack import check_price
    from SingleFlightTrack import send_email
    import time
    send_email()
    time.sleep(15)


