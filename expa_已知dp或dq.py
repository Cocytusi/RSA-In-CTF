# 已知dp或dq
import gmpy2
e = 65537
n = 9637571466652899741848142654451413405801976834328667418509217149503238513830870985353918314633160277580591819016181785300521866901536670666234046521697590230079161867282389124998093526637796571100147052430445089605759722456767679930869250538932528092292071024877213105462554819256136145385237821098127348787416199401770954567019811050508888349297579329222552491826770225583983899834347983888473219771888063393354348613119521862989609112706536794212028369088219375364362615622092005578099889045473175051574207130932430162265994221914833343534531743589037146933738549770365029230545884239551015472122598634133661853901
dp = 81339405704902517676022188908547543689627829453799865550091494842725439570571310071337729038516525539158092247771184675844795891671744082925462138427070614848951224652874430072917346702280925974595608822751382808802457160317381440319175601623719969138918927272712366710634393379149593082774688540571485214097
c = 5971372776574706905158546698157178098706187597204981662036310534369575915776950962893790809274833462545672702278129839887482283641996814437707885716134279091994238891294614019371247451378504745748882207694219990495603397913371579808848136183106703158532870472345648247817132700604598385677497138485776569096958910782582696229046024695529762572289705021673895852985396416704278321332667281973074372362761992335826576550161390158761314769544548809326036026461123102509831887999493584436939086255411387879202594399181211724444617225689922628790388129032022982596393215038044861544602046137258904612792518629229736324827

for i in range(1,65538):
    if (dp*e-1)%i == 0:
        if n%(((dp*e-1)//i)+1)==0:
            p=((dp*e-1)//i)+1
            q=n//(((dp*e-1)//i)+1)
            phi = (p-1)*(q-1)
            d = gmpy2.invert(e,phi)%phi
            m = gmpy2.powmod(c,d,n)
            print ('m:',m)
            print ('flag: ')
            print (bytes.fromhex('{:x}'.format(int(m))))