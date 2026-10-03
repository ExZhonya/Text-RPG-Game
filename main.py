import preset.wc_gb as wc
from map_ import Base

def main():
	wc.welc_asc()
	try:
		if wc.welc_text():
			while Base.camp():
				pass
	except KeyboardInterrupt:
		pass
	wc.bye_asc()
	wc.bye_text()

if __name__ == '__main__':
	main()