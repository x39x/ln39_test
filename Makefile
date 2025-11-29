ln1: 
	@make clean
	@LN1=1 python3 config.py


ln2: 
	@make clean && mkdir $(HOME)/39config
	@ln -s $(CURDIR)/fileB $(HOME)/39config/fileA
	@LN2=1 python3 config.py

fn: 
	@make clean
	@FUNC=1 python3 config.py

hang:
	@rm $(HOME)/39config/ln.hang || true
	@ln -s $(HOME)/no_such_file $(HOME)/39config/ln.hang
	@HANG=1 python3 config.py

bak:
	@make clean
	@mkdir -p $(HOME)/39config/dirA/ 
	@touch $(HOME)/39config/dirA/fileA 
	@touch $(HOME)/39config/fileA
	@BACKUP=1 python3 config.py

utils:
	UTILS=1 python3 config.py

clean:
	@trash $(HOME)/39config || true

