install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 brain_games

mytesting:
	make lint
	make install
	make build
	make publish
	make package-install

.PHONY: install brain-games brain-even build publish package-install lint mytesting

