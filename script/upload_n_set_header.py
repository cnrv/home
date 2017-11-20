import os

def print_script(cmd):
	print("echo EXEC: ./ossutil %s " % cmd)
	print("./ossutil -e $OSS_E -i $OSS_I -k $OSS_K %s " % cmd)
	print("")

os.chdir("_site")
print("#!/bin/sh")
print_script("rm -f oss://cnrv-website --recursive")
for root, dirs, files in os.walk("./"):
    for file in files:
    	if file.endswith("ossutil"):
		continue
	file_name = os.path.join(root, file)
	oss_file_name = "oss://cnrv-website/%s" % file_name[2:]
	print_script("cp -f '_site/%s' '%s'" % (file_name, oss_file_name))
        if file.endswith(".html"):
            print_script("cp -f '%s' '%s'" % (oss_file_name, oss_file_name[:-5]))
            print_script('set-meta "%s" --update "Content-Type:text/html; charset=utf-8"' % oss_file_name[:-5])

