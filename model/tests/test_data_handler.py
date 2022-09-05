""" Test for DataHandler CH4Cals being a subclass of it"""
import pandas as pd
import json
from model import advanced_controls
from model import ch4calcs
import pytest

from model.data_handler import DataHandler

@pytest.mark.skip(reason="ch4 updates have broken this example")
def test_ch4_tons_reduced():
    soln_net_annual_funits_adopted = pd.DataFrame(soln_net_annual_funits_adopted_list[1:],
                                                  columns=soln_net_annual_funits_adopted_list[0]).set_index(
        'Year')
    ac = advanced_controls.AdvancedControls(report_start_year=2020, report_end_year=2050,
                                            ch4_co2_per_funit=0.01, ch4_is_co2eq=False)
    c4 = ch4calcs.CH4Calcs(ac=ac, soln_net_annual_funits_adopted=soln_net_annual_funits_adopted)
    result = c4.ch4_tons_reduced()
    expected = pd.DataFrame(ch4_tons_reduced_list[1:],
                            columns=ch4_tons_reduced_list[0]).set_index('Year')

    is_data_handler = issubclass(type(c4), DataHandler)
    json_data = c4.to_json()
    existing_key = 'ch4_tons_reduced' in json_data

    pd.testing.assert_frame_equal(result.loc[2015:], expected, check_exact=False)
    assert is_data_handler == True
    assert existing_key == True
    pd.testing.assert_frame_equal(json_data['ch4_tons_reduced'].loc[2015:], expected, check_exact=False)

# 'Unit Adoption'!B251:L298
soln_net_annual_funits_adopted_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa", "Latin America",
     "China", "India", "EU", "USA"],
    [2015, 59.16952483163, -75.62640223557, -0.33768156367, -22.15920892112, -1.71009099271, -15.41714380040,
     -15.43313810117, -3.07011430874, -55.75969246529, -13.21605539049],
    [2016, 150.52159292976, -76.24855891557, -0.34297979401, -23.24591339780, -1.84510420765, -16.18366871191,
     -15.89405398012, -3.39192750636, -56.24733048614, -13.30746078097],
    [2017, 257.36122967139, -76.87071559558, -0.34827802435, -24.33261787447, -1.98011742258, -16.95019362342,
     -16.35496985906, -3.71374070399, -56.73496850699, -13.39886617146],
    [2018, 378.99298898654, -77.49287227559, -0.35357625469, -25.41932235115, -2.11513063752, -17.71671853493,
     -16.81588573801, -4.03555390161, -57.22260652784, -13.49027156194],
    [2019, 514.72142480523, -78.11502895560, -0.35887448503, -26.50602682782, -2.25014385245, -18.48324344644,
     -17.27680161696, -4.35736709924, -57.71024454869, -13.58167695243],
    [2020, 514.73678922371, -78.73718563561, -0.36417271537, -27.59273130450, -2.38515706739, -19.24976835795,
     -17.73771749591, -4.67918029686, -58.19788256953, -13.67308234291],
    [2021, 825.68654167325, -79.35934231562, -0.36947094570, -28.67943578117, -2.52017028232, -20.01629326946,
     -18.19863337485, -5.00099349449, -58.68552059038, -13.76448773340],
    [2022, 999.53233058261, -79.98149899563, -0.37476917604, -29.76614025785, -2.65518349726, -20.78281818097,
     -18.65954925380, -5.32280669212, -59.17315861123, -13.85589312388],
    [2023, 1184.69301171557, -80.60365567564, -0.38006740638, -30.85284473453, -2.79019671219, -21.54934309248,
     -19.12046513275, -5.64461988974, -59.66079663208, -13.94729851437],
    [2024, 1380.47313900213, -81.22581235565, -0.38536563672, -31.93954921120, -2.92520992713, -22.31586800399,
     -19.58138101170, -5.96643308737, -60.14843465293, -14.03870390485],
    [2025, 1433.94497468791, -81.84796903566, -0.39066386706, -33.02625368788, -3.06022314206, -23.08239291550,
     -20.04229689064, -6.28824628499, -60.63607267378, -14.13010929534],
    [2026, 1801.10994775612, -82.47012571567, -0.39596209740, -34.11295816455, -3.19523635700, -23.84891782701,
     -20.50321276959, -6.61005948262, -61.12371069462, -14.22151468583],
    [2027, 2024.57573708357, -83.09228239568, -0.40126032774, -35.19966264123, -3.33024957193, -24.61544273852,
     -20.96412864854, -6.93187268024, -61.61134871547, -14.31292007631],
    [2028, 2255.87918828469, -83.71443907569, -0.40655855808, -36.28636711790, -3.46526278687, -25.38196765003,
     -21.42504452749, -7.25368587787, -62.09898673632, -14.40432546680],
    [2029, 2494.32485528949, -84.33659575570, -0.41185678841, -37.37307159458, -3.60027600180, -26.14849256154,
     -21.88596040643, -7.57549907549, -62.58662475717, -14.49573085728],
    [2030, 2856.55316015211, -84.95875243571, -0.41715501875, -38.45977607125, -3.73528921674, -26.91501747306,
     -22.34687628538, -7.89731227312, -63.07426277802, -14.58713624777],
    [2031, 2989.86105243015, -85.58090911572, -0.42245324909, -39.54648054793, -3.87030243167, -27.68154238457,
     -22.80779216433, -8.21912547074, -63.56190079887, -14.67854163825],
    [2032, 3245.56069042605, -86.20306579573, -0.42775147943, -40.63318502461, -4.00531564661, -28.44806729608,
     -23.26870804327, -8.54093866837, -64.04953881971, -14.76994702874],
    [2033, 3505.62075994569, -86.82522247573, -0.43304970977, -41.71988950128, -4.14032886154, -29.21459220759,
     -23.72962392222, -8.86275186600, -64.53717684056, -14.86135241922],
    [2034, 3769.34581491907, -87.44737915574, -0.43834794011, -42.80659397796, -4.27534207648, -29.98111711910,
     -24.19053980117, -9.18456506362, -65.02481486141, -14.95275780971],
    [2035, 4036.04040927621, -88.06953583575, -0.44364617045, -43.89329845463, -4.41035529141, -30.74764203061,
     -24.65145568012, -9.50637826125, -65.51245288226, -15.04416320019],
    [2036, 4305.00909694713, -88.69169251576, -0.44894440079, -44.98000293131, -4.54536850635, -31.51416694212,
     -25.11237155906, -9.82819145887, -66.00009090311, -15.13556859068],
    [2037, 4575.55643186183, -89.31384919577, -0.45424263112, -46.06670740798, -4.68038172128, -32.28069185363,
     -25.57328743801, -10.15000465650, -66.48772892395, -15.22697398117],
    [2038, 4846.98696795034, -89.93600587578, -0.45954086146, -47.15341188466, -4.81539493622, -33.04721676514,
     -26.03420331696, -10.47181785412, -66.97536694480, -15.31837937165],
    [2039, 5118.60525914267, -90.55816255579, -0.46483909180, -48.24011636133, -4.95040815115, -33.81374167665,
     -26.49511919591, -10.79363105175, -67.46300496565, -15.40978476214],
    [2040, 5437.16953108051, -91.18031923580, -0.47013732214, -49.32682083801, -5.08542136609, -34.58026658816,
     -26.95603507485, -11.11544424937, -67.95064298650, -15.50119015262],
    [2041, 5659.62332255882, -91.80247591581, -0.47543555248, -50.41352531469, -5.22043458102, -35.34679149967,
     -27.41695095380, -11.43725744700, -68.43828100735, -15.59259554311],
    [2042, 5927.63220264268, -92.42463259582, -0.48073378282, -51.50022979136, -5.35544779596, -36.11331641118,
     -27.87786683275, -11.75907064462, -68.92591902820, -15.68400093359],
    [2043, 6193.04705355042, -93.04678927583, -0.48603201316, -52.58693426804, -5.49046101089, -36.87984132269,
     -28.33878271170, -12.08088384225, -69.41355704904, -15.77540632408],
    [2044, 6455.17242921204, -93.66894595584, -0.49133024350, -53.67363874471, -5.62547422583, -37.64636623420,
     -28.79969859064, -12.40269703988, -69.90119506989, -15.86681171456],
    [2045, 6713.31288355757, -94.29110263585, -0.49662847384, -54.76034322139, -5.76048744076, -38.41289114571,
     -29.26061446959, -12.72451023750, -70.38883309074, -15.95821710505],
    [2046, 6966.77297051701, -94.91325931586, -0.50192670417, -55.84704769806, -5.89550065570, -39.17941605722,
     -29.72153034854, -13.04632343513, -70.87647111159, -16.04962249553],
    [2047, 7214.85724402038, -95.53541599587, -0.50722493451, -56.93375217474, -6.03051387063, -39.94594096873,
     -30.18244622749, -13.36813663275, -71.36410913244, -16.14102788602],
    [2048, 7456.87025799770, -96.15757267588, -0.51252316485, -58.02045665141, -6.16552708557, -40.71246588024,
     -30.64336210643, -13.68994983038, -71.85174715329, -16.23243327651],
    [2049, 7692.11656637898, -96.77972935589, -0.51782139519, -59.10716112809, -6.30054030050, -41.47899079175,
     -31.10427798538, -14.01176302800, -72.33938517413, -16.32383866699],
    [2050, 7895.38590200891, -97.40188603589, -0.52311962553, -60.19386560477, -6.43555351544, -42.24551570326,
     -31.56519386433, -14.33357622563, -72.82702319498, -16.41524405748],
    [2051, 8139.52728207347, -98.02404271590, -0.52841785587, -61.28057008144, -6.57056673037, -43.01204061477,
     -32.02610974327, -14.65538942325, -73.31466121583, -16.50664944796],
    [2052, 8350.30079724671, -98.64619939591, -0.53371608621, -62.36727455812, -6.70557994531, -43.77856552628,
     -32.48702562222, -14.97720262088, -73.80229923668, -16.59805483845],
    [2053, 8551.52582254397, -99.26835607592, -0.53901431655, -63.45397903479, -6.84059316024, -44.54509043779,
     -32.94794150117, -15.29901581851, -74.28993725753, -16.68946022893],
    [2054, 8742.50691189525, -99.89051275593, -0.54431254688, -64.54068351147, -6.97560637518, -45.31161534930,
     -33.40885738012, -15.62082901613, -74.77757527838, -16.78086561942],
    [2055, 8922.54861923059, -100.51266943594, -0.54961077722, -65.62738798814, -7.11061959011, -46.07814026081,
     -33.86977325906, -15.94264221376, -75.26521329922, -16.87227100990],
    [2056, 9090.95549847998, -101.13482611595, -0.55490900756, -66.71409246482, -7.24563280505, -46.84466517233,
     -34.33068913801, -16.26445541138, -75.75285132007, -16.96367640039],
    [2057, 9247.03210357344, -101.75698279596, -0.56020723790, -67.80079694150, -7.38064601998, -47.61119008384,
     -34.79160501696, -16.58626860901, -76.24048934092, -17.05508179088],
    [2058, 9390.08298844099, -102.37913947597, -0.56550546824, -68.88750141817, -7.51565923492, -48.37771499535,
     -35.25252089591, -16.90808180663, -76.72812736177, -17.14648718136],
    [2059, 9519.41270701265, -103.00129615598, -0.57080369858, -69.97420589485, -7.65067244985, -49.14423990686,
     -35.71343677485, -17.22989500426, -77.21576538262, -17.23789257185],
    [2060, 9634.32581321841, -103.62345283599, -0.57610192892, -71.06091037152, -7.78568566479, -49.91076481837,
     -36.17435265380, -17.55170820188, -77.70340340347, -17.32929796233]]

# 'CH4 Calcs'!A10:K56 with O25 set to 'CH4'
ch4_tons_reduced_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa", "Latin America",
     "China", "India", "EU", "USA"],
    [2015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2016, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2017, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2018, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2019, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2020, 5.14736789224, -0.78737185636, -0.00364172715, -0.27592731304, -0.02385157067, -0.19249768358,
     -0.17737717496, -0.04679180297, -0.58197882570, -0.13673082343],
    [2021, 8.25686541673, -0.79359342316, -0.00369470946, -0.28679435781, -0.02520170282, -0.20016293269,
     -0.18198633375, -0.05000993494, -0.58685520590, -0.13764487733],
    [2022, 9.99532330583, -0.79981498996, -0.00374769176, -0.29766140258, -0.02655183497, -0.20782818181,
     -0.18659549254, -0.05322806692, -0.59173158611, -0.13855893124],
    [2023, 11.84693011716, -0.80603655676, -0.00380067406, -0.30852844735, -0.02790196712, -0.21549343092,
     -0.19120465133, -0.05644619890, -0.59660796632, -0.13947298514],
    [2024, 13.80473139002, -0.81225812356, -0.00385365637, -0.31939549211, -0.02925209927, -0.22315868004,
     -0.19581381012, -0.05966433087, -0.60148434653, -0.14038703905],
    [2025, 14.33944974688, -0.81847969036, -0.00390663867, -0.33026253688, -0.03060223142, -0.23082392916,
     -0.20042296891, -0.06288246285, -0.60636072674, -0.14130109295],
    [2026, 18.01109947756, -0.82470125716, -0.00395962097, -0.34112958165, -0.03195236357, -0.23848917827,
     -0.20503212770, -0.06610059483, -0.61123710695, -0.14221514686],
    [2027, 20.24575737084, -0.83092282396, -0.00401260328, -0.35199662641, -0.03330249572, -0.24615442739,
     -0.20964128649, -0.06931872680, -0.61611348715, -0.14312920076],
    [2028, 22.55879188285, -0.83714439076, -0.00406558558, -0.36286367118, -0.03465262787, -0.25381967650,
     -0.21425044527, -0.07253685878, -0.62098986736, -0.14404325467],
    [2029, 24.94324855289, -0.84336595756, -0.00411856788, -0.37373071595, -0.03600276002, -0.26148492562,
     -0.21885960406, -0.07575499075, -0.62586624757, -0.14495730857],
    [2030, 28.56553160152, -0.84958752436, -0.00417155019, -0.38459776071, -0.03735289217, -0.26915017473,
     -0.22346876285, -0.07897312273, -0.63074262778, -0.14587136248],
    [2031, 29.89861052430, -0.85580909116, -0.00422453249, -0.39546480548, -0.03870302432, -0.27681542385,
     -0.22807792164, -0.08219125471, -0.63561900799, -0.14678541638],
    [2032, 32.45560690426, -0.86203065796, -0.00427751479, -0.40633185025, -0.04005315647, -0.28448067296,
     -0.23268708043, -0.08540938668, -0.64049538820, -0.14769947029],
    [2033, 35.05620759946, -0.86825222476, -0.00433049710, -0.41719889501, -0.04140328862, -0.29214592208,
     -0.23729623922, -0.08862751866, -0.64537176841, -0.14861352419],
    [2034, 37.69345814919, -0.87447379156, -0.00438347940, -0.42806593978, -0.04275342076, -0.29981117119,
     -0.24190539801, -0.09184565064, -0.65024814861, -0.14952757810],
    [2035, 40.36040409276, -0.88069535836, -0.00443646170, -0.43893298455, -0.04410355291, -0.30747642031,
     -0.24651455680, -0.09506378261, -0.65512452882, -0.15044163200],
    [2036, 43.05009096947, -0.88691692516, -0.00448944401, -0.44980002931, -0.04545368506, -0.31514166942,
     -0.25112371559, -0.09828191459, -0.66000090903, -0.15135568591],
    [2037, 45.75556431862, -0.89313849196, -0.00454242631, -0.46066707408, -0.04680381721, -0.32280691854,
     -0.25573287438, -0.10150004656, -0.66487728924, -0.15226973981],
    [2038, 48.46986967950, -0.89936005876, -0.00459540861, -0.47153411885, -0.04815394936, -0.33047216765,
     -0.26034203317, -0.10471817854, -0.66975366945, -0.15318379372],
    [2039, 51.18605259143, -0.90558162556, -0.00464839092, -0.48240116361, -0.04950408151, -0.33813741677,
     -0.26495119196, -0.10793631052, -0.67463004966, -0.15409784762],
    [2040, 54.37169531081, -0.91180319236, -0.00470137322, -0.49326820838, -0.05085421366, -0.34580266588,
     -0.26956035075, -0.11115444249, -0.67950642986, -0.15501190153],
    [2041, 56.59623322559, -0.91802475916, -0.00475435552, -0.50413525315, -0.05220434581, -0.35346791500,
     -0.27416950954, -0.11437257447, -0.68438281007, -0.15592595543],
    [2042, 59.27632202643, -0.92424632596, -0.00480733783, -0.51500229791, -0.05355447796, -0.36113316411,
     -0.27877866833, -0.11759070645, -0.68925919028, -0.15684000934],
    [2043, 61.93047053550, -0.93046789276, -0.00486032013, -0.52586934268, -0.05490461011, -0.36879841323,
     -0.28338782712, -0.12080883842, -0.69413557049, -0.15775406324],
    [2044, 64.55172429212, -0.93668945956, -0.00491330243, -0.53673638745, -0.05625474226, -0.37646366234,
     -0.28799698591, -0.12402697040, -0.69901195070, -0.15866811715],
    [2045, 67.13312883558, -0.94291102636, -0.00496628474, -0.54760343221, -0.05760487441, -0.38412891146,
     -0.29260614470, -0.12724510238, -0.70388833091, -0.15958217105],
    [2046, 69.66772970517, -0.94913259316, -0.00501926704, -0.55847047698, -0.05895500656, -0.39179416057,
     -0.29721530349, -0.13046323435, -0.70876471112, -0.16049622496],
    [2047, 72.14857244020, -0.95535415996, -0.00507224935, -0.56933752175, -0.06030513871, -0.39945940969,
     -0.30182446227, -0.13368136633, -0.71364109132, -0.16141027886],
    [2048, 74.56870257998, -0.96157572676, -0.00512523165, -0.58020456651, -0.06165527086, -0.40712465880,
     -0.30643362106, -0.13689949830, -0.71851747153, -0.16232433277],
    [2049, 76.92116566379, -0.96779729356, -0.00517821395, -0.59107161128, -0.06300540301, -0.41478990792,
     -0.31104277985, -0.14011763028, -0.72339385174, -0.16323838667],
    [2050, 78.95385902009, -0.97401886036, -0.00523119626, -0.60193865605, -0.06435553515, -0.42245515703,
     -0.31565193864, -0.14333576226, -0.72827023195, -0.16415244057],
    [2051, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2052, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2053, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2054, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2055, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2056, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2057, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2058, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2059, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2060, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]