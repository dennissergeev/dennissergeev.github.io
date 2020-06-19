BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/_site
NB_DIR=$(BASEDIR)/blog/_notebooks
NB_OUTPUT_DIR=$(BASEDIR)/_blog
NB_TOOLS_DIR=$(BASEDIR)/_nb_tools

IMG_DIR=$(BASEDIR)/images

GITHUB_PAGES_BRANCH=master

install:
	sudo apt install ruby-dev ruby-bundler nodejs
	bundle install

serve:
	bundle exec jekyll liveserve	

clean:
	bundle clean
	rm -rf $(OUTPUTDIR)/* .*~

notebook : ${NB}
	python $(NB_TOOLS_DIR)/connect_notebook_to_post.py $< --title="${TITLE}" --thumbnail=${THUMBNAIL}
	jupyter nbconvert --to markdown $< --template=$(basename $<).tpl --output-dir=$(NB_OUTPUT_DIR)
	@if [ -d $(NB_OUTPUT_DIR)/$(basename $(notdir $<))_files ]; then \
	cp -r $(NB_OUTPUT_DIR)/$(basename $(notdir $<))_files $(IMG_DIR) && rm -r $(NB_OUTPUT_DIR)/$(basename $(notdir $<))_files; \
	fi

.PHONY: clean install serve
