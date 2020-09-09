func  main（）{
	标志。解析（）
	//初始化日志
	如果 * ver {
		普通的。PrintVersion（）
		返回
	}
	如果 err  ：=  beego。LoadAppConfig（“INI” ，文件路径。加入（常见。GetRunPath（），“CONF” ，“nps.conf” ））; err  ！=  nil {
		日志。Fatalln（“加载配置文件错误”，错误。错误（））
	}
	普通的。InitPProfFromFile（）
	如果 level  =  beego。AppConfig。字符串（“ log_level”）; 级别 ==  “” {
		等级 =  “ 7”
	}
	日志。重设（）
	日志。EnableFuncCallDepth（true）
	日志。SetLogFuncCallDepth（3）
	logPath  ：=  beego。AppConfig。字符串（“ log_path”）
	如果 logPath  ==  “” {
		logPath  =  common。GetLo
