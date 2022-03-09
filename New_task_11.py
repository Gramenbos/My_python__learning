# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
seconds = int(input('Enter number of seconds: '))
days = int(seconds / 86400)
seconds -= days * 86400
hours = int(seconds / 3600)
seconds -= hours * 3600
minutes = int(seconds / 60)
seconds -= minutes * 60
print(f'{days}:{hours}:{minutes}:{seconds}')
