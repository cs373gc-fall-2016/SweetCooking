.DEFAULT_GOAL := test

FILES :=                              \
    html/SweetCooking.html                      \
    SweetCooking.log                       

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

SweetCooking.html: app/helpers.py
	pydoc3 -w SweetCooking

SweetCooking.log:
	git log > SweetCooking.log

RunSweetCooking.tmp: SweetCooking.py RunSweetCooking.in RunSweetCooking.out RunSweetCooking.py .pylintrc
	-$(PYLINT) SweetCooking.py
	-$(PYLINT) RunSweetCooking.py
	$(PYTHON) ./RunSweetCooking.py < RunSweetCooking.in > RunSweetCooking.tmp
	diff RunSweetCooking.tmp RunSweetCooking.out

TestSweetCooking.tmp: SweetCooking.py TestSweetCooking.py .pylintrc
	-$(PYLINT) TestSweetCooking.py
	$(COVERAGE) run    --branch TestSweetCooking.py >  TestSweetCooking.tmp 2>&1
	$(COVERAGE) report -m                      >> TestSweetCooking.tmp
	cat TestSweetCooking.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  SweetCooking.html
	rm -f  SweetCooking.log
	rm -f  RunSweetCooking.tmp
	rm -f  TestSweetCooking.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i SweetCooking.py
	$(AUTOPEP8) -i RunSweetCooking.py
	$(AUTOPEP8) -i TestSweetCooking.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: SweetCooking.html SweetCooking.log check
