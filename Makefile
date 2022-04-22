run: main.py
	python3 main.py -b data

test: test_restrieve_phone_numers.py
	python3 -m unittest -b