import  re , os , string ,  getopt ,sys , unittest,logging

def setup_env() :
    root  = os.path.dirname(os.path.realpath(__file__))
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)
    root  = os.path.dirname(root)

    sys.path.append(os.path.join(root,"src") )
    sys.path.append(os.path.join(root,"test") )

    os.environ['PRJ_ROOT'] = os.environ['HOME'] + "/devspace/rigger-ng"
    logging.basicConfig(level=logging.DEBUG,filename='test.log')

    import core.run_env
    core.run_env.set_modul_path()
    core.run_env.load_rgenv()


if __name__ == '__main__':

    setup_env()

    import interface,impl
    impl.setup()
    import websys
    websys.setup()

    from websys.tc.port_tc  import *


    # from ubuntu.mysql_tc  import *
    # from ubuntu.varnishd_tc  import *
    # from ubuntu.fpm_tc  import *
    # from ubuntu.websvc_tc   import *
    unittest.main()
    #  try :
    #  except yaml.constructor.ConstructorError as e :
        #  rgio.error(e)
    #  except interface.user_break as e:
        #  rgio.error(e)
    #  except interface.badargs_exception  as e :
        #  print("\nerror:")
        #  rgio.error(e)
        #  runargs.help()
    #  except getopt.GetoptError as e:
        #  print("\nerror:")
        #  print(e)
        #  runargs.help()
    #  except interface.depend_exception as e :
        #  e.monitor.out()
    #  except interface.cmd_use_error as e :
        #  rgio.error(e)
        #  rgio.simple_out("useage:")
        #  cmdobj = impl.rg_ioc.ins_cmd(e.cmd)
        #  cmdobj.useage(rgio.simple_out)
    #  except interface.res_use_error as e :
        #  rgio.error(e)
        #  rgio.simple_out("useage:")
        #  res = impl.rg_ioc.ins_res(e.res)
        #  res.useage(rgio.simple_out)
#
    #  except interface.rigger_exception as e:
         #  rgio.error(e)
