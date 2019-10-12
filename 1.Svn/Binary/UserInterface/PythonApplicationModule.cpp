// 1.) Find this:
#ifdef ENABLE_COSTUME_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_COSTUME_SYSTEM",	0);
#endif

// 2.) Add after this:
#ifdef ENABLE_ITEM_EMOTION
	PyModule_AddIntConstant(poModule, "ENABLE_ITEM_EMOTION",	1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_ITEM_EMOTION",	0);
#endif