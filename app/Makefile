UI_FILES = $(wildcard ui/*.ui)
PY_FILES = $(patsubst %.ui,%.py,$(UI_FILES))

ui: $(PY_FILES)

ui/%.py: ui/%.ui
	pyuic5 -o $@ $<

run: ui
	python3 main.py

clean:
	rm ui/*.py
