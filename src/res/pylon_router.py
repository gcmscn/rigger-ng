#coding=utf-8
import logging
import interface
import os

from utls.rg_io  import rg_logger
from utls.rg_sh  import shexec
from string import *

_logger = logging.getLogger()

class pylon_router(interface.resource):
    """
    生成 pylon rest 的索引
    !R.rest
        src: "$${PRJ_ROOT}/src/apps/api"
    """
    def _before(self,context):
        self.out_idx    = os.path.join(self.dst , "_rest_conf.idx")
    def _config(self,context):

        sed     = """sed -r "s/.+:class\s+(\S+)\s+.+\/\/\@REST_RULE:\s+(.+)/\\2 : \\1/g" """
        cmdtpl  = """grep --include "*.php" -i  -E "class .+ implements XService"  -R $SRC   |  """  + sed + " > $DST "

        cmd     = Template(cmdtpl).substitute(SRC = self.src ,DST = self.out_idx)
        shexec.execmd(cmd,False)

    def _check(self,context):
        self.check_print(os.path.exists(self.out_idx),self.out_idx)

    def clean_file(self,filename):
        cmdtpl = "if test -e $DST ; then rm -f  $DST ; fi ; "
        cmd    = Template(cmdtpl).substitute(DST=filename)
        shexec.execmd(cmd)

    def _clean(self,context):
        self.clean_file(self.out_idx)

