BEGIN TRANSACTION;CREATE TABLE cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );INSERT INTO "cars" VALUES(1,'Renault',22200);INSERT INTO "cars" VALUES(2,'Volvo',29200);INSERT INTO "cars" VALUES(3,'Mercedes',57200);INSERT INTO "cars" VALUES(5,'Audi',52200);INSERT INTO "cars" VALUES(7,'Chevrolet',46200);INSERT INTO "cars" VALUES(8,'Daewoo',38200);INSERT INTO "cars" VALUES(9,'Citroen',29200);INSERT INTO "cars" VALUES(10,'Honda',33200);INSERT INTO "cars" VALUES(12,'Chevrolet',46200);INSERT INTO "cars" VALUES(13,'Daewoo',38200);INSERT INTO "cars" VALUES(14,'Citroen',29200);INSERT INTO "cars" VALUES(15,'Honda',33200);INSERT INTO "cars" VALUES(16,'Renault',22100);INSERT INTO "cars" VALUES(17,'���������',1000);CREATE TABLE cost (
        name TEXT, tr_in INTEGER, buy INTEGER
    );INSERT INTO "cost" VALUES('����',17,2);CREATE TABLE users (
        name TEXT,
        ava BLOB,
        score INTEGER
    );INSERT INTO "users" VALUES('����',X'89504E470D0A1A0A0000000D4948445200000080000000800806000000C33E61CB00001E3B4944415478DAED9D09585357F6C0836DED36B6FD665A9D4E9DD1B1CB2CEDFCDB8EEF0554DC10ADBB85E0022401C50501B52A2A6AAD4BC51D1414051736111112F2C2A682B228526D296EECFB1296B0246C7599A2E7FFDD17030112B2F0F212D47CDFF95A249CDCDCDF79F79E7BEEB9E7322C2D270DB6B49CF41AA31F2FF4F7CFF40C36BC3E30598CC58DE2E0C2D91C5CB88A83115E6C9CCFE3E0BC340ECECBE6E0FC1A0EC6977070413B1717824C88762E4648B8B8B0868B13F7B9B820958B0923B998D00BE9706012B3904EA4DBF8BE6F3FF50D74F85CB3D88FB8B870010713FA704713191C4CD82A07CBC109E0E0D14A84802EF89A0B1B235A39383FC31EE7F9DA33236CEDB18011CFD7C333001AEF3031E50D075C389D048E090B54C1A21A7E1FFAF2B9387198830BBE71FB24E1F597F0F5A06FFEBF2307A3219D8B13A15C8C68E9072CAAE1F7789FB099830943D094B17C74C06B2FE1F7539FA369ECA71C8CD8C7C5883AAA61E95D1F46D491A3142EFCFC257C2DF5B14713E65C8C88E5E2C4535A60E9591F0727D2D99860CEC89161262FE1ABD03776ACEDEB6C66840D1B236E1B12967EF5F1B2ECB10816FAAE2FE12BE8B3C723E6B031FEAFC6054B8FFA307EA63D337CD60B0F7F2133E80B36C68F376A58FAD597C4C662BF78E1E02F1AB3FB3D3616759883F17F7F81E1CB570EFFE360C4FEF966916FBE10F0EDF0F0E96C9C57321061E9571F51C4660A2DE8E641DB87B126EF1F628F451E60E3D14F5EC25725C4530E4E042C1F1DF3165DD3302DF0EDCDC2FECBC67839CF172CFDE963E3C27B8AF1037D3AE07A87CFC622D91C9CDFFE12BE96FA30E103362E70D077DC406FF0ADAC7C5E61E3513E2F042C3DEA636351DE56D8DC37F41E37A012BEF57F4E0F6663BCC897F0A9D1C7C67804F2A106047CD6E7A17F6063BC4463EEDCA566E1E03DE53B10CEB6800CAB7F408EF5FB506EF30654DBBC0A35D6265063CD801A960954B3064195CD60C8630D85D479A3E1B0A5BBC18C898D11C9F6CC84778C1AFE4253DE3014EE3436F8CE66E7E0CC3447B8F9EDBFA084F516547E6B0215CF04FD7FF5B70CA8B1D24C2A6D5E8753D3961A6424E160C24CF618FE504A97F254C1E79A468DE4E0FC226380EF682A003FCB5590FEED97506AF336090E415604AF0B7C454999871B66CB793451E8602A1849591C870AF80E5F093FE0E0D1F9F2462F318D0027B3705AE1AF1D1700D1B36641AECD3072F8568445357CB9BEF019D60631760E2E2C76C0E3FE4C49D0A8BFF06D99D1EFC887FD956383209DFD25D4B9BC0A6297C17065D144D83FF97BBD74C632D3F310307505F99457D8BCA91616D5F0919E72EB57C1C194D7D93EF771C7493FE18789FBC08919A5D7918E8311771DBE14BC67D09C40E4ED73705E92BCD167E7D94283AB09485C1920756390FF459D5666F336C4CE9E0A1BC7FBEADC192E6342C979FC27ABCF497DDAC2A21ABE5C84B32C2187D57BD441526A33042ECE990CCE6667F5E2E370306172CF3434DAF60ADC3E701DC4C1F8518A0DBFC5FD77277CB9D45A77EF1491CD6B709F351CD2E661E4907D62AA331C99B20E0E4F594B7AE6472D9DE1DC746B48983D1E32BEFD1714B0FE0822D23BEF3F2CAAE16BAAAF9A650231B3BF01475C40FDEA012304F3E747BE42FB4651CF200F17E743ADF39BDDE09306B06060C1D2A7BEB2F96F83BBB99F1EB29505FB69856F8F47707A367EC598B05EF0913438BC84DF6D0464BD0A3B26EEA278F5C07F8A328DE8818F367670FE6F3D1BEF362E58A901485D195037FF257C457DE5D6AFC0C6F1DED4AE1E307EA31DF3E428BDC247E14836CEBFAFCC721733A341E266A2D40824CE0CA89D3F3060D5B218506B8322810CA862994085957EDA57C27A13969B9DA578E9C8BFE5881FD48F0120CBB2C7A3FCFA1AB644CE43948F02485C1820B63302F8D6B21109B5A59ECB8046270648963340E2A260B0AE0C7235532F171713102F378106470688ED65C64145FB6E5B8DA43C6E80D2E8F5021F65F2A0B9A6AF61EB16F74BD506F04C1A973240B4801EF8680552B78001F56C06342C6640D30A0648D4B4AF177C57936E4B5BF97B90E1D451E0E01EB374A3384E423CE560311329854FE6F0E1FC62757356E05C278D3B57BCC2046AB826205A6802D5D614C0B73281AA052650636F02F5CF60AB33465DE0F794A665CFA60C1D4726B4B7A0B83CA42468841139EA4E2669B5914026706AE0B0AC1FEF0F125713ED3BD795014DCB19D0B89801623603C4B60C102F62401D92853D64916CF846EFAB7534813A2713A85BA1192CAAE1779BDED8BA4F4BE767D8501F2EC6041B28C909B4350BFC3F361EFD3F4DBDD564BB71D4762ED5B0F4A80F4D33BAF838283E4075B8988313BFD97D1D37A2DF39816C8C77499BA5CAC609C7A0C96DD00B07BFD3C771D2CDC1DD356937E5E1620E268CEA574E203AB1A3CB3A95CFB27A21E1CBF5D52ED1DEC14D99C7D44B3E84031E3345A79C40F2AC1ECEFB459775EA12533EDC76F8F485842FD7851C5C6D56372536EFE82BD3E8864E9941E8A0667F82146BCCFDA168D9FB2F247CB9BEDA455AAC6AAC4D3A570354EF15D831F9E3B54E0BA3E294EEDAF17E50BCFCFDE703FEE60FA1F5C21A90BABFABB13EC94A5964515323D83AC14B2F69662847534BF8D1965445A8D68E3F0EB94BFE3670E1AF1F02AD415C68BF1E04ED374241BAEE2DADF421A7505303F0B35CA9B73433367E6EACC639816C8CB8486578D2C9340A2E2EB01C50F09B37BC0BADFE56D09EEA4F82978B74F5AB5AEB43F10B4D825A21D317EAF1487A9450A39C405496455F9539BCBED904C5CB861935FCE66D23A0356C79E713DF4DD24340BACA44EBF6A120972611CD8899F3F49863C87FCA191DF5B1DA9C407454599F098D4B9851103A8F0B152BDE331EF86BDF82165F4B688BDDD51BBAA25C0FD4B97DE245EAC3C567A72FD06B822907273CFB0C07A2F8311B236AE948DD5E62CA8360961B34EFF8C430F0DDDF8516EF89D01AF91DB45D3BDD37F867D2961E028DAB5FD7A97D4D4BD5EF159C98BA54AFD9C5886D9F7B04A890119D8736823744C93AF7D201680E6041E3F64FA1DEF515BDC06F70FF1334EE3385963376D016B78B1CCE3581AE08BFF95A1034B8EBBEB455CC8950162EDE32619FDE53CB518D459506C0C188B3749ED8C9397FAE5BE74AD382409AE407924877683A610DD2FDA6D0FCC34890AEFF43DF9D8B1CB3F543C8A55AF3AE7F42F3C1B1D074742634052D06097F2B48938E91FADBB484DE133E6A5FC3F7237536CE46357B054B9891FA3F57801141CA0F774C4C7983CE228CEB6608A02DBD07FC67A214567A30B45F3D0A6D970FC924D11BDA534EF472D634D6A7037CD2007EFC8FEE23930B03AAAD54EF15B88E09A1E350891415DEEC6D00B8703A9D0735433745F6EADCBCE8C3C03BB4118E6E5A06FBD67061E74A3BD8B1D20E4E6E73817B515E5AC3D2047E53CA19288BF703495AA046FA1AF7E2FD9A96AA17A9DE28DA647E9496E3731C8CB05432FC93552D693BA57BEBD4B9CECE6D4C3E0347DC9DC076C66452EC665AF412FB5916501A7B8C52F857FCB7937A917ECE6C4BD8B66C219CDFB396FC1C55FAA4DBFEDE27E4E6EF06F7E993D438AADE28DA31C1939E83B31871A8B7018C260AE982EF68468038A9AB6333CFED57099F3D6B0AB82C9C0DFB563B40534A2065F091C41CF1506E6C332DC07FEB4A68483ED34B9F74DDDBAAE16FFD8BAC3D69A7A02DDE13DACEBB42CB91C920593DB82B136AA5EA5DC283161EF438E01891D3FD64AFACE43A6DE7F3B72F88EC06ABFEEA6938BDDD157C372D239FC0B4D3BBE0CE85435079D11F5AAE07533EEC2B4A599C1FC41FFD9EFCECD576733B0D1149E04EB7EEFA928FF7F9F4B79EB155DA3E69AC2788D7FDB173F520B251BE4BB867F20FB439E0F6A3F91F2A0CFF82857456BE08DF725E2F0E1A15FA32C30FC0F1ADCEB0D9693E84ED5DDB4D5F5BCC0ED506B0CA04DA920EAB6C9F247243E7EAA1CE567950C863BC0F6D3E980316C3EA73FED767F1838C80B346095F9DBED6F095AA87FF6D23D4EAAB75FF48E60BA8382DB5724C286D3E181B27BC3B8380E8A60D3ACB9E54C4850C38F8485A4EB2541A40CBE1496AF535ECC655EF105A33682D93C3C67937C88CA0ED8CED83B8B8B08D2EF8AE53F85AC1429EBADF9615507DD9DFA0F091341F1CA77AFE0F7650ABAF7EFB17B2B0B0B3B213C483E8AD3E864737A3AC2F06FB6BE12774163CDACBB9A0312CB446E7CCB1243DF3631ECBD5C212787B902B0A4DE12307F37E94374852353326E9B651AA0D20CABDEFF6A59C00C9AAC19D47E57A1A40B9CD5BB417A05A80057DD219FFA7ABE05198C7058D01A155807C698696827DC1972FE98E6F5EA1F1932F8F3DF86D5EA1D148225DFFAEEA2980D8A6BA7DE921D072686C574CC0A5B701DC630DA7BDFA181BBF3087E1800B56D359EDEAEA91F35A0DD16E8B669390DC16CD51091FFDBC8C35833480F37BD76904BFFA7200F97EA47B95FD3C8DA611C9A68F5406799AE3F72A6D5F5BD21168D937BAD7FBFBCA0AA691C74AB401E44567B5AB3BA1615A19C0AFE7F6C3BE350E9011B247E5309D7C7247E748912F38A2D19C7F2FD2AB73BDFF83B3AD46D352DD9E05506DF726342C7BB51BCC3AE7D7419ADA236874F518B4F84E83E635BD2383E87C624F03089B616B88D2730718B24B15E92B7556767C7BB74E6D4D3B034D897ED078C9179A2E1F83E694935DEB6E0D1DB45DAE6C12FE7AAE95C60E1F0A3EA1271FFD5DCAC99D1A19A3E87B16E44FF9809482A9EF43E99C77A1C4FA1DC89B3E0CA4A981B2F625FA905BCE7DED602A9B02506129DAEB0E8E262E30D818FF1A5DF01733F950B66A6AD7909A7402AA799EBDA4267A2F345CF481E6B440B5F00B091FB09F35850479E180BB56DE7E43F269105DF2D778342A5F3EAED300F2A67C00D9A40C25A5E9D231D9BEC6DA21EA93439C7BAE005E31CC6515983099D1BD8CBB7E93115CC78441C1B43F436BD20968BB114A82566600A2A8DD5071E147A88CDA03F5978FF7E9A0A125A26CB3680A94C71FD75FDC203D180AE78C500A1F494DF056684C38ACD1AE203AB9DCCD01B41E6E98A29318719741DEA54B5391C38D134E911D58BB7F31B45E0FEA137EB982D425F82A8585402EB1FA8634806D2B16E93568D4747E974AF8E8E76ABFD5507B6E836689214BBB670645CE9C6D90C2D51C8C1031504080AE0A971EE38F939D58F4ED28684B0B845A62BF5AF8E867F4EF2DA9BDF3F672F8873B9D3FBED7468DE1B7A20D9AAB01501F7F186A055D6DA8E1798238E6204892D048D2DD40445BAC54C247FF5E7D6829D406B968768A98DB3D336883F961C394D7C508095A053CA0AB9CEB16739FCE39B4CE6725E900D6090FA8858F7E8F80F5048C9244E406E0BDDE09C4574EF5095F9A16483A9BAAA61E4511C7797739AA29A7217FE6DF54C247DFA76AE722A83BE5A89101A0323372F865ACD70D565B191D2167703161075D859C3DCC8E741A00390A20A8E9A1E413574D1C848AC8DD4AE1A391824C09EB199ABD160C6BECE675DBCB473F271CDBDA1B7EEA19A811EC570B5E519A53640655EDC9EE133E92CA2DF3A0CE6F8166C9A1365D6961A9F3BE34E0F5B6C20EAD0DA03FDEEA7AD3139D1D8644E431B7FB939A1A483A7D757147A03EEE30F9B44AAF9C80B6EBAAE76BB40A5863DF6504685DEFB37159AF61BFF1F231ADE0239124F98134F608E4CCF86B9FF09194AF9F01629F39EAD3C25C1850A950796CF7E46D862BA9FFCC001ED0950AEE621AD2ADD3F22C87426D80BB5A07ADED5A10D4FBAD86AA0DB3A0628D2529551BE740CD5E2E3404AC8746FE3EC808DA05F147B7407AE06E684A0DECA50F2DD3B43680C4E350E888AB858FA4CC6512D41F9AA23627B06E8962A9B8B70C7A9F023905A02BCFE94A05776246F65A47E77EF317A83DE3A112BE246A0F14DB7CD6ABC37B4A9EE530C8B7FA0C0A179B4299FB6C1079AD0071F84E684D3D239BC7AF07414DF43E8DE1D7C77A41C92A4B8DE023297599080DFBC6A83DA720B2EF5E68DAA09769904E202EACA6331B38DBF2AFBDBCE99C19C3A129DEA717FCE6182F2898315C3DFC3EBC73F4F7956BBF01297F1FB45D0F86A64B477BAD3EC815007F0FD41207A031C10724177DA178C5788DE19306B0660A34FEF895DA432A5536CF0CC07A10AC300B35EC353AA385550C2E4EDCA7331B387532AE1456C577D3FA8CBCF512CBA16AE1F77C7FCD2EBBCE1341ADD782A025F50CB9126953C83BAC3FB311F2AD3FD30A3E39056CB582A6ED9FF509BF6E79574268C2EC494670351D71078D00297466A2444E98ADBC732D8782D8D7A56BAF3EF67027E49E52E5310FDAAE058234D61BC4415B4174C4192A76D842E977D3A090331AF2FB18356AF670A0F58A7FB713BF68A4117BAF8062FBAF3433262552E9B5141A370FEFF3785A355B06BF92351896E07C835FA0C5C60457503E60149D992827CC9D5477AEE550106DB586964B47417C6C958A277F18B4259F8238DF2DB0C1914526742873209BE37DA064FF52285CF8B9523D05D33E2497A22834ADD548A24CD7D461507DEE0768DAF0A73E0FA65659A3A29826E039698751DC9E86AEF643AB002F3A3351F68EF5D0A873E5607AFDFBCCE1246494B18B967C0E73A642ACEF6632C823878F52BD0FAE7524F7078803EBA168FE3F75F621F2359062CE7F65AB86B56FAB848FBC7F91F5203860B1D968EE25B4C7220FA22960159D99289BCC0E69D5B9CA603544ED8522A12F38CE9DDAB9A7FF1DFB5B32B3C7D38D439EF2916F1065851F800AD7497A834F3A806BA74175D46E90AE1AA4BA60D44206C4CE9E66549752B2F148376400B3E9CC44716686F40B3E8253B8C4149AAE9C84CC7307C8543165278AB8732C4178D8039A8587A070FA5FF4069F0C02FDB808AA2377AA848F367FC89AC0A602A3814F1A00F3FC6CC6622C6E14DD99283F4DFEB7CEF0E5A00AECBF0271E836F25C61BCEF1672C8777760912340D4C10D501DE707E2A36E9D5BB8FA824F3A80475DC9B075FDAAD794168F285BF40E6C1D7FD0E8AEB7B5679E1EC56030C08483095AE8DC8F8E9860DD2FF88AB08A59FF20D7F9A26D3650BD6321546D9E0765CBC6AA7CEAA9864F86B4C3B6917B1775EBBB8A47FCEAF809785AEE80DD5376C252D328A3838F7681478E0C33919D0CC2F91974EE471F1CEB4109FCFE4C2354E9CB9F3BAA7317B366AF79E793EF3FD3D9C82FB6165C57B80984E74BE79664CF4DA1810A9FFC3BE7095D3B98E1DFC375F6D77065D1788DEF0030D8ADE6F223E264516866842D9D5B92A873EE5B0C1FF0F0D1DF97ECB6EF328048CF0174A53D61D5650058C008BA77A592268E1DF0F0B32D3F84F290AD5DF90BBCBD03043E2A16F5ECEE61799D400E4614D0D9787FF3E5031BFE94A190B798D92D7945C4DB3F20E0733022BB579D400E2E3C4267E3D79B1D1FD0F09194EC75E896B924E21F307AF8CFDE77B07789185CF00DDD8D578C070C34F8B9F34641F9F99D9DF09154F10E1A3D7C659748C82E83FE24E1753A9343901C37771990F091147DCFEA061F4965D421A387AFB24CDCB34A212174367E297E016E5B8C1870F073E77E0CA2889DBD924ACA23BD8C1AFE3339A3B252A80393984577E34F8D771850F0D1CF659E6CA56964A511DEC60E1FB8CC98692A0D60E2C49457B9B8B086CEC62F659E830C8BCF060CFC22475C651E6149F861A386AFB658F4B37AC1FBE86EFCAEB1DB0704FCFC197F85AAE04D2A0DA0F0DC11E37DF26569E0BBD5DE162A2B19D37561045D8DE74F9861D4F0F3A60C25D3BEFACA24CE3BEB6BBCF071E229DAF9D5E8CA582E268CA7BBF1CB9811707DD257460A5F96F4A92E953C27C4D748E19312A3F19DC16CA6D0C2108D77330D825F2C3E333AF8A5EE33343A4B702FF0A8B1C2077BA660BC56770773705E96211ABFC1F4186459FCDD38E05B0E85328F391A1F26C93AE96794F0B9387153EBBB83EDB10896A11ABFC6F414644CFEC2C0F0FF0CE5BBEDB43A4AF68BFF7123848F4AC10866EA7477301BE7FF6CA8C6AF608643E2A47106815F307B24340479407D9C9756069071F484F1C1C7899F51D697D67707CBF204C26719B2F10E4C02BCC7AD837B16C369835FBE7222792EA1F3804ACA69A88FF5560B1F8585530F1F372AF8E4DA9F29B4D0E9EE60F92FE52B0243EE72AD363D05719326E9157EDEDC8FA1DE5F758D4154A1A421C1873C43A8AAACCDE503278C0A3E171746F40BBE425CE0B131EC72B99B1D81880973E0DE946194C1CFB7FE07880E38914FBA461546AF059347CD6BF87B7B553649D8E36F34F03998B015DD03D12FF8DA5E26499703B4C6340002CC97419A054E0668B4859F3B6B0494AC9E0A3527D641333A1CAA43A1E9B6F46068BC74142AA33C3B53C284BB4E1ACB938FFE669D467CD5C147AFF966916F7271A2C890F097980B619B531A04FAE44052622DDC2B6883CAE60EA82CAD84F2783E94F87B42F11607C8E18C83FBB618642FFC1A72E77E0AF76D71C85A65053777AD81BC036E203EBBA3B3AA271555C6256941204686C0DB03BCEF4F19077C8CC876C40FBEA6C9C3CD50075F3138A4EA4E617DC177991E0FBE3B3321294904C5E20750D9D20155AD4F54CA757107C456F79618D1EF40543C848BA54DD0785D3F975548AF0581EFB20B46F0E40B9FD831F9E33582AFECEEE03E378A94A48D510D7F89792C7879DC84E4641194363C84B2A647502679A416FE9DA6277DC227CA657223B700A4D782F572BFC05EB6111CF9C6059E1AC3571B0E549235848A0AE8A3F16BE626C185E022C817B5CBA0CB4503F895AD4F20B1563D7C522A1E4256EE7DBD5C2EB16B61B4A1CFFBFFC4325FF996C6F075797171E1E75C9C68A7AAF19B16A5C0C55811944B7F27616B0B1F4941B3E6F0D1BFA3DF671614426BC639CAE08B7F11C2F9B43AE0E5FE065E7E85B0725622CD0EB3A061A1D9C9BFEB157ED754106D45DE47DF8FC6A3273E4E502973E45A3A74868FE46E8FE15F1D7CB9A4958AA1E196A05FF0DB32CE42767616C48B1E776F43D5EFB0FBC77B74C17FCAC623AC68812F9F36D85894B74EA5E2A65D82A8D012286FFA5D367CF7133E92DB8D4FB4862F97F8EAFFC1EDBC1C90FE74412BF82D37C2A0E86E3A24973729D52B17BF63F9E0601AA35787D91E8FDA472B7CF42156D8DC3738382F52D3C62F9B100FA17EF9502C7EDC357753009F1C01244F7482DFCD10448FE166511994DE4903C9CD48A5F0C5E911509C7905B272B3E15265BB5A9D48AED43E81AC9C1638B8E167E032F5B15AE2472016B4C2970B7238381871495D43F77D7713B24BDABB3B6E14C1475224ED1F7CA50651F900AE14D5C195C26AB85C520F09A5529DF4C5557740458BECFB66DCAA876D4EA9D4C1C778C9B6A3B70D31087CF9872D194B0CE160C24CA5C3FDD44B9078B1A6B7D74E217C24152D1D9050451D7CAA8DA95CE1FB96363E0221AF04564E8BEF277C7EE6BCD1BBFF6850F8F297EDE898F7B9B8305FB191EE36C970AFA85DEFF0E5FA6ED63C324AF88935CA573779950FC89151B74B1FA38B59634E0C370AF89D670A4C0523E53790AF9A990839A5BFD1061FE9296E7A04F195C6051FFDDD2F757D7FDFE8F03270328FD3A2B41BBF10DDF76754F01596877F5A6F7D35EB7E511BADF0E572B7FE11C41A11FC44916CC857F77DB3B25B60B35DAA46C3FE8271C73EA20ABEDA08A12E4B8B385EE9889FB32412BAE1CBF5DD561112A61B7E42E543286CD0FCFBA265B19747669F0E1F6BEC91F7A984DF674E607FD695C78E65FFE1EAD5BA52BAE1CBDF734FF204E26A0C07FF52D523ADE0777DB7271072344FC9528F176D3DD9F31DAAE1ABCD09ECCF87A14BA9A3CE965C296D7C482BFCCEA561B36C0D4E37FCF49A8750D2D8BFEF2B8C2C07C731B164840F0579A85CE76B951348C58745471478E68BDA9FD2095F7193088589B5D928D215FE65D163B8DB40DD487739A1FA913D163E976A1EFDCA0CD2F5C3CEF86599DFB855D74227FC9E8690237902D7EB51E8975AF889A2077057DC6307B39FF07FBE2B693F7BFAEED4E702BE5C9F9F5FD61B31FC8A24F91E005DF07B395BCD1D70A7FE115CAB7E08972A1F815007F8C888AE893BE07ED31372338BAAF655347740BCB03273E7CEC0F79E2BF88ABF0FF12B70BE5BD8FAD810F095E943F1831C4907DC697C02B71A3AC85122552C931471075CAD938D1CE87728E9245FDA413A6B54B7EF5E51DBA3F0D3F92BE9E6C1A0F5C39EBD12121ADFB97CB1FA6249C3FF9E1A12BE31E82BA97F0C71828AABC78FFF3A8476F8DAE404521D3442AF8880A2FF265DAA2944C3E88B083F3DA3B1EE7C40D158438CC43AE504521D3492BFCE9D2874CBBC2B6D7D51E0DFCC6C6A8D0C295A67A86958E79C407DC0EF36220416B9A6A4D5D497363E9FF06FFEDAD4C60F2BD9A9EFA537EDC92154373ED43F9B7D35595456DCF070C0C32F977640DAF5FAFA50DFFC8D74F5DF8086AFA82FCABFD82C29B12625BBA4FDF78106FF5E616B470CBF22EDF481DC3186EABF010D5FF1F7CB9767BE167A347FEDC5F8CADCBCF2DF9E182BFCBC8ADF9E2627D7154604176EDEBE3D7BB0B1F4DF8086DFF3E5B536E3CDC8A0E20D9713AA7FF9394BF2000DB186849F95DDF23021A6F2E659BF8255DB1D52DE30F6FE1BD0F095BD7CDC333F0E0B28D8154F54DDBC714BDC925BDEFA545FF0732B5A9FA6673448620595372F0415EE093E59F4F940EFBFE7A6F18AFA0E6D49619EF2BEE31E155A1C9220ACCA484BABAFB899D924BD9DD3F230B7ECB78EC2EA874F4BEA1F3F953B69E8E79C92F627F70BDB7ECFBC277D70F3D7A6E6C4C4AA3221AF38232234372CE4C49D2DA77D6E4F0A0F0F3379DEFAEFFF01DC0147016AF0DF130000000049454E44AE426082',1000);DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('cars',17);COMMIT;