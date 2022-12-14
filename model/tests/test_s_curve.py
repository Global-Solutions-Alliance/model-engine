"""Tests for s_curve.py."""

from model import s_curve
import numpy as np
import pandas as pd
import pytest




def test_sigmoid_logistic():
    """Test logistic sigmoid, simple case."""
    sc = s_curve.SCurve(transition_period=None, sconfig=None)
    # values from Building Automation System "S Curve Adoption"!AH17:AH22
    result = sc._sigmoid_logistic(base_year=2014, last_year=2050,
                                  base_percent=0.346959145052, last_percent=0.95,
                                  base_adoption=16577.8259167003, last_pds_tam=77969.4257883872)
    expected = pd.DataFrame(world_sigmoid_logistic_list[1:],
                            columns=world_sigmoid_logistic_list[0]).set_index('Year')
    pd.testing.assert_frame_equal(result, expected, check_exact=False)



def test_sigmoid_logistic_100_percent_final_adoption():
    """Test logistic sigmoid, with 100% last_percent adoption."""
    sc = s_curve.SCurve(transition_period=None, sconfig=None)
    # values from Building Automation System "S Curve Adoption"!AJ17:AJ22
    result = sc._sigmoid_logistic(base_year=2014, last_year=2050,
                                  base_percent=0.677494504097, last_percent=1.0,
                                  base_adoption=14915.990000000000, last_pds_tam=30578.7612542884)
    expected = pd.DataFrame(OECD90_sigmoid_logistic_list[1:],
                            columns=OECD90_sigmoid_logistic_list[0]).set_index('Year')
    pd.testing.assert_frame_equal(result, expected, check_exact=False)
    result = sc._sigmoid_logistic(base_year=2014, last_year=2050,
                                  base_percent=0.677494504097, last_percent=0.999999999999,
                                  base_adoption=14915.990000000000, last_pds_tam=30578.7612542884)
    pd.testing.assert_frame_equal(result, expected, check_exact=False)



def test_sigmoid_logistic_divide_by_zero():
    """Test logistic sigmoid, with 100% last_percent adoption."""
    sc = s_curve.SCurve(transition_period=None, sconfig=None)
    result = sc._sigmoid_logistic(base_year=2014, last_year=2050,
                                  base_percent=0.1, last_percent=0.0,
                                  base_adoption=1000.0, last_pds_tam=1000.0)
    expected = pd.DataFrame(nan_sigmoid_logistic_list[1:],
                            columns=nan_sigmoid_logistic_list[0]).set_index('Year')
    pd.testing.assert_frame_equal(result, expected, check_exact=False)
    with pytest.warns(None) as warnings:
        result = sc._sigmoid_logistic(base_year=2014, last_year=2050,
                                      base_percent=np.float64(0.1), last_percent=np.float64(0.0),
                                      base_adoption=1000.0, last_pds_tam=1000.0)
    assert len(warnings) == 0
    pd.testing.assert_frame_equal(result, expected, check_exact=False)

def test_logistic_adoption():
    # From Building Automation System "S Curve Adoption"!AJ17:AJ22
    sconfig = pd.DataFrame([
        ['World', 2014, 2050, 0.346959145052, 0.95, 16577.8259167003, 77969.4257883872],
        ['OECD90', 2014, 2050, 0.677494504097, 1.0, 14915.99, 30578.7612542884],
        ['Eastern Europe', 2014, 2050, 0.0, 0.212709603444, 325.933926458798, 1532.2953039347],
        ['Asia (Sans Japan)', 2014, 2050, 0.074153999059, 0.447707349074, 1087.77094452167, 25358.3339750411],

        ['Middle East and Africa', 2014, 2050, 0.0, 0.085083841378, 0.0, 4140.6610709308],
        ['Latin America', 2014, 2050, 0.0, 0.223853674537, 0.0, 1021.9329224435],
        ['China', 2014, 2050, 0.0848, 0.0, 1087.77094452167, 18965.135056084],
        ['India', 2014, 2050, 0.0, 0.0, 0.0, 8804.235498036],
        ['EU', 2014, 2050, 0.482603137947, 1.0, 3622.85, 11003.3574757203],
        ['USA', 2014, 2050, 0.445634302889, 1.0, 11293.14, 36879.9583966390]],
        columns=['region', 'base_year', 'last_year', 'base_percent', 'last_percent',
                 'base_adoption', 'last_pds_tam']).set_index('region')
    sc = s_curve.SCurve(transition_period=16, sconfig=sconfig)
    result = sc.logistic_adoption()
    expected = pd.DataFrame(logistic_s_curve_adoption_list[1:],
                            columns=logistic_s_curve_adoption_list[0]).set_index('Year')
    expected.name = 'logistic_adoption'
    pd.testing.assert_frame_equal(result, expected, check_exact=False)



def test_bass_diffusion():
    # From Water Efficiency Measures "S Curve Adoption"!B119:K128
    sconfig = pd.DataFrame([
        ['World', 2014, 2050, 0.5, 86258.8944386277, 499769.3997737280, 0.0011209600, 0.1033334410],
        ['OECD90', 2014, 2050, 0.5558684888, 47682.0319026127, 165775.7429560840, 0.0011209600, 0.1033334410],

        ['Eastern Europe', 2014, 2050, 0.0, 0.0, 21474.3917595734, 0.0011209600, 0.1033334410],
        ['Asia (Sans Japan)', 2014, 2050, 0.0, 0.0, 188212.6206588630, 0.0011209600, 0.1033334410],
        ['Middle East and Africa', 2014, 2050, 0.0, 0.0, 62742.1062748580, 0.0011209600, 0.1033334410],

        ['Latin America', 2014, 2050, 0.0, 0.0, 45343.3516130736, 0.0011209600, 0.1033334410],
        ['China', 2014, 2050, 0.0, 0.0, 77612.1430465617, 0.0011209600, 0.1033334410],
        ['India', 2014, 2050, 0.0, 0.0, 45491.8656042331, 0.0011209600, 0.1033334410],
        ['EU', 2014, 2050, 0.0, 0.0, 59700.4155768868, 0.0011209600, 0.1033334410],
        ['USA', 2014, 2050, 0.0, 0.0, 64756.7863759130, 0.0011209600, 0.1033334410]],
        columns=['region', 'base_year', 'last_year', 'base_percent', 'base_adoption',
                 'last_pds_tam', 'innovation', 'imitation']).set_index('region')
    sc = s_curve.SCurve(transition_period=None, sconfig=sconfig)
    result = sc.bass_diffusion_adoption()
    expected = pd.DataFrame(bass_diffusion_adoption_list[1:],
                            columns=bass_diffusion_adoption_list[0]).set_index('Year')
    expected.name = 'bass_diffusion_adoption'
    pd.testing.assert_frame_equal(result, expected, check_exact=False)



def test_bass_diffusion_regions_NaN():
    # From Bioplastics "S Curve Adoption"!B119:K128
    sconfig = pd.DataFrame([
        ['World', 2014, 2050, 0.00536977491961415, 1.67, 791.974792264998, 0.00112096, 0.10333344],
        ['OECD90', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Eastern Europe', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Asia (Sans Japan)', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Middle East and Africa', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Latin America', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['China', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['India', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['EU', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['USA', 2014, 2050, 0.0, 0.0, 0.0, 0.0, 0.0]],
        columns=['region', 'base_year', 'last_year', 'base_percent', 'base_adoption',
                 'last_pds_tam', 'innovation', 'imitation']).set_index('region')
    sc = s_curve.SCurve(transition_period=None, sconfig=sconfig)
    result = sc.bass_diffusion_adoption()
    expected = pd.DataFrame(bass_diffusion_adoption_regions_NaN_list[1:],
                            columns=bass_diffusion_adoption_regions_NaN_list[0]).set_index('Year')
    expected.name = 'bass_diffusion_adoption'
    pd.testing.assert_frame_equal(result, expected, check_exact=False)


def test_bass_diffusion_base_year_2018():
    # From SmartThermostats 2021
    sconfig = pd.DataFrame([
        ['World', 2018, 2050, 0.031982286536317, 29.0761830722887, 2512.33209193275, 0.001677824, 0.246469535],
        ['OECD90', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Eastern Europe', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Asia (Sans Japan)', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Middle East and Africa', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['Latin America', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['China', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['India', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['EU', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0],
        ['USA', 2018, 2050, 0.0, 0.0, 0.0, 0.0, 0.0]],
    columns=['region', 'base_year', 'last_year', 'base_percent', 'base_adoption',
                 'last_pds_tam', 'innovation', 'imitation']).set_index('region')
    sc = s_curve.SCurve(sconfig=sconfig)
    result = sc.bass_diffusion_adoption()
    expected = pd.DataFrame(bass_diffusion_base_year_2018_list[1:],
                            columns=bass_diffusion_base_year_2018_list[0]).set_index('Year')
    expected.name = 'bass_diffusion_adoption'
    pd.testing.assert_frame_equal(result, expected, check_exact=False)


# Building Automation System "S Curve"!AH24:AI70
world_sigmoid_logistic_list = [
    ["Year", "first_half", "second_half"],
    [2014, 16577.825917, 35116.538355], [2015, 17354.241330, 36279.528816],
    [2016, 18196.959474, 37472.977969], [2017, 19108.111120, 38691.996375],
    [2018, 20089.231761, 39931.226537], [2019, 21141.208736, 41184.930237],
    [2020, 22264.245394, 42447.090802], [2021, 23457.844491, 43711.526609],
    [2022, 24720.812013, 44972.011376], [2023, 26051.281506, 46222.396297],
    [2024, 27446.757872, 47456.728978], [2025, 28904.178534, 48669.364323],
    [2026, 30419.988970, 49855.063101], [2027, 31990.228988, 51009.074752],
    [2028, 33610.625725, 52127.202019], [2029, 35276.689309, 53205.846083],
    [2030, 36983.807289, 54242.032029], [2031, 38727.334396, 55233.415426],
    [2032, 40502.674797, 56178.271702], [2033, 42305.354698, 57075.470578],
    [2034, 44131.083882, 57924.438278], [2035, 45975.805503, 58725.110375],
    [2036, 47835.734057, 59477.878170], [2037, 49707.381994, 60183.531279],
    [2038, 51587.575861, 60843.198857], [2039, 53473.463111, 61458.291500],
    [2040, 55362.510921, 62030.445486], [2041, 57252.498404, 62561.470591],
    [2042, 59141.503581, 63053.302366], [2043, 61027.886435, 63507.959412],
    [2044, 62910.269204, 63927.505885], [2045, 64787.514949, 64314.019269],
    [2046, 66658.705284, 64669.563228], [2047, 68523.117957, 64996.165258],
    [2048, 70380.204886, 65295.798732], [2049, 72229.571039, 65570.368924],
    [2050, 74070.954499, 65821.702523], [2051, 75904.207910, 66051.540205],
    [2052, 77729.281423, 66261.531789], [2053, 79546.207200, 66453.233587],
    [2054, 81355.085482, 66628.107550], [2055, 83156.072170, 66787.521870],
    [2056, 84949.367856, 66932.752746], [2057, 86735.208225, 67064.987036],
    [2058, 88513.855709, 67185.325589], [2059, 90285.592300, 67294.787047],
    [2060, 92050.713406, 67394.311976]]

# Building Automation System "S Curve"!AJ24:AK70
OECD90_sigmoid_logistic_list = [
    ["Year", "first_half", "second_half"],
    [2014, 14915.990000, 21597.317876], [2015, 15308.190503, 23234.255421],
    [2016, 15749.186640, 24112.576831], [2017, 16198.683572, 24507.360171],
    [2018, 16644.384724, 24670.589828], [2019, 17085.531217, 24735.734073],
    [2020, 17523.711203, 24761.364527], [2021, 17960.281174, 24771.391918],
    [2022, 18396.049770, 24775.306271], [2023, 18831.438919, 24776.832983],
    [2024, 19266.654149, 24777.428245], [2025, 19701.791472, 24777.660306],
    [2026, 20136.894487, 24777.750769], [2027, 20571.982595, 24777.786034],
    [2028, 21007.064295, 24777.799780], [2029, 21442.143263, 24777.805139],
    [2030, 21877.221075, 24777.807228], [2031, 22312.298402, 24777.808042],
    [2032, 22747.375526, 24777.808360], [2033, 23182.452565, 24777.808483],
    [2034, 23617.529569, 24777.808532], [2035, 24052.606558, 24777.808550],
    [2036, 24487.683541, 24777.808558], [2037, 24922.760522, 24777.808561],
    [2038, 25357.837502, 24777.808562], [2039, 25792.914482, 24777.808562],
    [2040, 26227.991461, 24777.808562], [2041, 26663.068441, 24777.808562],
    [2042, 27098.145420, 24777.808562], [2043, 27533.222399, 24777.808562],
    [2044, 27968.299379, 24777.808562], [2045, 28403.376358, 24777.808562],
    [2046, 28838.453337, 24777.808562], [2047, 29273.530316, 24777.808562],
    [2048, 29708.607296, 24777.808562], [2049, 30143.684275, 24777.808562],
    [2050, 30578.761254, 24777.808562], [2051, 31013.838234, 24777.808562],
    [2052, 31448.915213, 24777.808562], [2053, 31883.992192, 24777.808562],
    [2054, 32319.069171, 24777.808562], [2055, 32754.146151, 24777.808562],
    [2056, 33189.223130, 24777.808562], [2057, 33624.300109, 24777.808562],
    [2058, 34059.377089, 24777.808562], [2059, 34494.454068, 24777.808562],
    [2060, 34929.531047, 24777.808562]]

nan_sigmoid_logistic_list = [
    ["Year", "first_half", "second_half"],
    [2014, np.nan, np.nan], [2015, np.nan, np.nan],
    [2016, np.nan, np.nan], [2017, np.nan, np.nan],
    [2018, np.nan, np.nan], [2019, np.nan, np.nan],
    [2020, np.nan, np.nan], [2021, np.nan, np.nan],
    [2022, np.nan, np.nan], [2023, np.nan, np.nan],
    [2024, np.nan, np.nan], [2025, np.nan, np.nan],
    [2026, np.nan, np.nan], [2027, np.nan, np.nan],
    [2028, np.nan, np.nan], [2029, np.nan, np.nan],
    [2030, np.nan, np.nan], [2031, np.nan, np.nan],
    [2032, np.nan, np.nan], [2033, np.nan, np.nan],
    [2034, np.nan, np.nan], [2035, np.nan, np.nan],
    [2036, np.nan, np.nan], [2037, np.nan, np.nan],
    [2038, np.nan, np.nan], [2039, np.nan, np.nan],
    [2040, np.nan, np.nan], [2041, np.nan, np.nan],
    [2042, np.nan, np.nan], [2043, np.nan, np.nan],
    [2044, np.nan, np.nan], [2045, np.nan, np.nan],
    [2046, np.nan, np.nan], [2047, np.nan, np.nan],
    [2048, np.nan, np.nan], [2049, np.nan, np.nan],
    [2050, np.nan, np.nan], [2051, np.nan, np.nan],
    [2052, np.nan, np.nan], [2053, np.nan, np.nan],
    [2054, np.nan, np.nan], [2055, np.nan, np.nan],
    [2056, np.nan, np.nan], [2057, np.nan, np.nan],
    [2058, np.nan, np.nan], [2059, np.nan, np.nan],
    [2060, np.nan, np.nan]]

# BuildingAutomation "S Curve Adoption"!A23:K70
logistic_s_curve_adoption_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa", "Latin America",
     "China", "India", "EU", "USA"],
    [2014, 16577.8259167003, 14915.9900000000, np.nan, 1087.7709445217, np.nan, np.nan, np.nan, np.nan, 3622.8500000000,
     11293.1400000000],
    [2015, 17354.2413299090, 15308.1905031352, np.nan, 1132.2599615581, np.nan, np.nan, np.nan, np.nan, 3781.9912229986,
     11821.7401657854],
    [2016, 18196.9594737997, 15749.1866401823, np.nan, 1182.9959225503, np.nan, np.nan, np.nan, np.nan, 3990.2613374196,
     12542.0144207409],
    [2017, 19108.1111195264, 16198.6835719345, np.nan, 1240.4943386935, np.nan, np.nan, np.nan, np.nan, 4211.3125498862,
     13316.8694257675],
    [2018, 20089.2317607510, 16644.3847244498, np.nan, 1305.2994994260, np.nan, np.nan, np.nan, np.nan, 4428.9144483078,
     14078.9498149532],
    [2019, 21141.2087356893, 17085.5312173207, np.nan, 1377.9845857676, np.nan, np.nan, np.nan, np.nan, 4641.1621893850,
     14819.3109424942],
    [2020, 22264.2453936230, 17523.7112031835, np.nan, 1459.1515476811, np.nan, np.nan, np.nan, np.nan, 4849.8272691294,
     15544.9840509925],
    [2021, 23457.8444911786, 17960.2811741666, np.nan, 1549.4307121413, np.nan, np.nan, np.nan, np.nan, 5056.5642316908,
     16262.7510492323],
    [2022, 24720.8120133816, 18396.0497695204, np.nan, 1649.4800874940, np.nan, np.nan, np.nan, np.nan, 5262.3592871926,
     16976.6668177375],
    [2023, 26051.2815057288, 18831.4389187311, np.nan, 1759.9843291132, np.nan, np.nan, np.nan, np.nan, 5467.7180414837,
     17688.8054525313],
    [2024, 27446.7578715725, 19266.6541491127, np.nan, 1881.6533314747, np.nan, np.nan, np.nan, np.nan, 5672.8813480370,
     18400.1512681489],
    [2025, 28904.1785335790, 19701.7914715219, np.nan, 2015.2204126715, np.nan, np.nan, np.nan, np.nan, 5877.9591047861,
     19111.1515145438],
    [2026, 30419.9889700206, 20136.8944870876, np.nan, 2161.4400592613, np.nan, np.nan, np.nan, np.nan, 6083.0000506912,
     19822.0036940405],
    [2027, 31990.2289875214, 20571.9825953828, np.nan, 2321.0852022828, np.nan, np.nan, np.nan, np.nan, 6288.0253657875,
     20532.7932651317],
    [2028, 33610.6257248870, 21007.0642947860, np.nan, 2494.9439994444, np.nan, np.nan, np.nan, np.nan, 6493.0441135783,
     21243.5566415937],
    [2029, 35276.6893094652, 21442.1432628945, np.nan, 2683.8161039876, np.nan, np.nan, np.nan, np.nan, 6698.0601259607,
     21954.3091531540],
    [2030, 36983.8072891849, 21877.2210754762, np.nan, 2888.5084076379, np.nan, np.nan, np.nan, np.nan, 6903.0750072288,
     22665.0571907486],
    [2031, 38727.3343958606, 22312.2984022113, np.nan, 3109.8302534502, np.nan, np.nan, np.nan, np.nan, 7108.0894236420,
     23375.8033973387],
    [2032, 40502.6747972467, 22747.3755257547, np.nan, 3348.5881242124, np.nan, np.nan, np.nan, np.nan, 7313.1036500214,
     24086.5488585254],
    [2033, 42305.3546976476, 23182.4525647112, np.nan, 3605.5798233690, np.nan, np.nan, np.nan, np.nan, 7518.1177990709,
     24797.2940176479],
    [2034, 44131.0838816783, 23617.5295685973, np.nan, 3881.5881780223, np.nan, np.nan, np.nan, np.nan, 7723.1319167792,
     25508.0390548548],
    [2035, 45975.8055034035, 24052.6065579949, np.nan, 4177.3743072916, np.nan, np.nan, np.nan, np.nan, 7928.1460218304,
     26218.7840430305],
    [2036, 47835.7340570042, 24487.6835414260, np.nan, 4493.6705138685, np.nan, np.nan, np.nan, np.nan, 8133.1601217862,
     26929.5290115496],
    [2037, 49707.3819940769, 24922.7605224070, np.nan, 4831.1728716513, np.nan, np.nan, np.nan, np.nan, 8338.1742196966,
     27640.2739722105],
    [2038, 51587.5758605750, 25357.8375023846, np.nan, 5190.5335974275, np.nan, np.nan, np.nan, np.nan, 8543.1883167879,
     28351.0189297382],
    [2039, 53473.4631105004, 25792.9144819521, np.nan, 5572.3533091821, np.nan, np.nan, np.nan, np.nan, 8748.2024135522,
     29061.7638860193],
    [2040, 55362.5109214659, 26227.9914613524, np.nan, 5977.1732871604, np.nan, np.nan, np.nan, np.nan, 8953.2165101860,
     29772.5088418056],
    [2041, 57252.4984040132, 26663.0684406847, np.nan, 6405.4678656845, np.nan, np.nan, np.nan, np.nan, 9158.2306067679,
     30483.2537973959],
    [2042, 59141.5035809613, 27098.1454199893, np.nan, 6857.6370932691, np.nan, np.nan, np.nan, np.nan, 9363.2447033292,
     31193.9987529086],
    [2043, 61182.8909962657, 27361.0090344781, np.nan, 7527.4672430466, np.nan, np.nan, np.nan, np.nan, 9552.4896642631,
     31894.3299669894],
    [2044, 63037.4237889585, 27569.4880265518, np.nan, 8201.9337372665, np.nan, np.nan, np.nan, np.nan, 9716.1078631254,
     32505.8180616256],
    [2045, 64698.7345092964, 27723.5823962128, np.nan, 8877.7745053186, np.nan, np.nan, np.nan, np.nan, 9854.0992999180,
     33028.4630368243],
    [2046, 66161.4197697651, 27823.2921434624, np.nan, 9551.4799875799, np.nan, np.nan, np.nan, np.nan, 9966.4639746416,
     33462.2648925883],
    [2047, 67420.9452388150, 27868.6172683010, np.nan, 10219.3075306154, np.nan, np.nan, np.nan, np.nan,
     10053.2018872965, 33807.2236289188],
    [2048, 68473.5525785758, 27859.5577707287, np.nan, 10877.2992174127, np.nan, np.nan, np.nan, np.nan,
     10114.3130378828, 34063.3392458163],
    [2049, 69316.1701134664, 27796.1136507457, np.nan, 11521.3029823285, np.nan, np.nan, np.nan, np.nan,
     10149.7974264006, 34230.6117432808],
    [2050, 69946.3285109946, 27678.2849083519, np.nan, 12146.9967765711, np.nan, np.nan, np.nan, np.nan,
     10159.6550528500, 34309.0411213125],
    [2051, 70362.0823256843, 27506.0715435474, np.nan, 12749.9154689451, np.nan, np.nan, np.nan, np.nan,
     10143.8859172309, 34298.6273799114],
    [2052, 70561.9379013169, 27279.4735563321, np.nan, 13325.4800914573, np.nan, np.nan, np.nan, np.nan,
     10102.4900195433, 34199.3705190776],
    [2053, 70544.7878410808, 26998.4909467061, np.nan, 13869.0289733050, np.nan, np.nan, np.nan, np.nan,
     10035.4673597872, 34011.2705388109],
    [2054, 70309.8520330195, 26663.1237146694, np.nan, 14375.8502525616, np.nan, np.nan, np.nan, np.nan,
     9942.8179379626, 33734.3274391115],
    [2055, 69856.6250513722, 26273.3718602220, np.nan, 14841.2152149053, np.nan, np.nan, np.nan, np.nan,
     9824.5417540696, 33368.5412199793],
    [2056, 69184.8296346776, 25829.2353833639, np.nan, 15260.4118847675, np.nan, np.nan, np.nan, np.nan,
     9680.6388081081, 32913.9118814144],
    [2057, 68294.3758607557, 25330.7142840950, np.nan, 15628.7782873874, np.nan, np.nan, np.nan, np.nan,
     9511.1091000781, 32370.4394234166],
    [2058, 67185.3255893752, 24777.8085624154, np.nan, 15941.7348107286, np.nan, np.nan, np.nan, np.nan,
     9315.9526299797, 31738.1238459861],
    [2059, 67294.7870471389, 24777.8085624154, np.nan, 16308.5960953450, np.nan, np.nan, np.nan, np.nan,
     9315.9526299797, 31738.1238459861],
    [2060, 67394.3119759907, 24777.8085624154, np.nan, 16671.1839505851, np.nan, np.nan, np.nan, np.nan,
     9315.9526299797, 31738.1238459861]]

# Water Efficiency Measures "S Curve Adoption"!A129:K176
bass_diffusion_adoption_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa",
     "Latin America", "China", "India", "EU", "USA"],
    [2014, 86258.8944386277, 47682.0319026127, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2015, 94097.4170719128, 51324.3642950798, 24.0719341868, 210.9788192538, 70.3313914499, 50.8280834242,
     87.0001078695, 50.9945616677, 66.9217778451, 72.5897672559],
    [2016, 102444.8291822980, 55114.2058935939, 50.6015321733, 443.4978688253, 147.8433822403, 106.8455438078,
     182.8826351582, 107.1954971656, 140.6760449095, 152.5907064529],
    [2017, 111306.2329074390, 59039.9733443160, 79.8332534663, 699.6997176380, 233.2502139912, 168.5685593738,
     288.5311005439, 169.1206753653, 221.9424169101, 240.7399938631],
    [2018, 120681.7472075130, 63087.6611898911, 112.0344743993, 981.9277894765, 327.3330848160, 236.5616974091,
     404.9118480549, 237.3365126927, 311.4642200562, 337.8439122579],
    [2019, 130565.8468412210, 67240.9383691080, 147.4973320574, 1292.7425240965, 430.9455367496, 311.4418077283,
     533.0807113323, 312.4618793426, 410.0536172989, 444.7834113298],
    [2020, 140946.7605174130, 71481.3280597478, 186.5406485564, 1634.9382425958, 545.0190779486, 393.8820858036,
     674.1899683052, 395.1721757182, 518.5969579714, 562.5199104235],
    [2021, 151805.9636409550, 75788.4714765730, 229.5119222441, 2011.5605993246, 670.5690004173, 484.6162772023,
     829.4955377332, 486.2035506381, 638.0603134762, 692.1013030724],
    [2022, 163117.8030199870, 80140.4712061940, 276.7893671138, 2425.9244563599, 808.7003386005, 584.4429838255,
     1000.3643499998, 586.3572216806, 769.4951470089, 834.6681069243],
    [2023, 174849.2905695500, 84514.3043639003, 328.7839753341, 2881.6319605741, 960.6138955106, 694.2300189561,
     1188.2818014472, 696.5038444946, 914.0440475441, 991.4596833712],
    [2024, 186960.0999010130, 88886.2907826320, 385.9415701402, 3382.5905362324, 1127.6122406972, 814.9187419554,
     1394.8591738800, 817.5878616947, 1072.9464370274, 1163.8204281158],
    [2025, 199402.7933750740, 93232.5971163664, 448.7448072627, 3933.0304265457, 1311.1055578565, 947.5282842962,
     1621.8408680723, 950.6317427356, 1247.5441344972, 1353.2058065512],
    [2026, 212123.2976461420, 97529.7546504376, 517.7150724350, 4537.5213243998, 1512.6171888119, 1093.1595561649,
     1871.1112616855, 1096.7400036370, 1439.2866312969, 1561.1880757608],
    [2027, 225061.6332291070, 101755.1671419790, 593.4142102048, 5200.9875245505, 1733.7886846123, 1252.9988968612,
     2144.7009574902, 1257.1028693394, 1649.7358973002, 1789.4614978108],
    [2028, 238152.8888767890, 105887.5853744250, 676.4460051975, 5928.7209061784, 1976.3841333660, 1428.3212024973,
     2444.7921369071, 1432.9994116480, 1880.5704989346, 2039.8468065522],
    [2029, 251328.4156655580, 109907.5272986680, 767.4573211232, 6726.3909157301, 2242.2934880967, 1620.4923310204,
     2773.7226765731, 1625.7999621319, 2133.5887657052, 2314.2946423360],
    [2030, 264517.2000596930, 113797.6264308000, 867.1387852615, 7600.0505661007, 2533.5345666159, 1830.9705475089,
     3133.9886221893, 1836.9675621546, 2410.7106931153, 2614.8876161028],
    [2031, 277647.3614357030, 117542.8961768860, 976.2248871206, 8556.1373013258, 2852.2533397751, 2061.3067324903,
     3528.2445450889, 2068.0581718735, 2713.9782169438, 2943.8406068910],
    [2032, 290647.7091257200, 121130.9034285380, 1095.4933398280, 9601.4673994871, 3200.7220656318, 2313.1430335137,
     3959.3012341960, 2320.7193173968, 3045.5534378657, 3303.4988360893],
    [2033, 303449.2882435250, 124551.8505427770, 1225.7635322208, 10743.2224060313, 3581.3347668931, 2588.2095967255,
     4430.1201016122, 2596.6868116533, 3407.7143181460, 3696.3331996596],
    [2034, 315986.8431712750, 127798.5701453940, 1367.8938794694, 11988.9259132738, 3996.5994901873, 2888.3189726898,
     4943.8036073158, 2897.7791418903, 3802.8473161757, 4124.9322788491],
    [2035, 328200.1327764910, 130866.4416422780, 1522.7778616974, 13346.4088408277, 4449.1267320308, 3215.3577519032,
     5503.5809420543, 3225.8890777923, 4233.4363735397, 4591.9903945101],
    [2036, 340035.0417032990, 133753.2416004530, 1691.3385251622, 14823.7612411147, 4941.6133728296, 3571.2749539916,
     6112.7881536636, 3582.9720226484, 4702.0476278854, 5100.2910252140],
    [2037, 351444.4463494750, 136458.9421473000, 1874.5212113292, 16429.2685732350, 5476.8214332898, 3958.0666750933,
     6774.8418686941, 3971.0306104505, 5211.3091992071, 5652.6848815193],
    [2038, 362388.8108793600, 138985.4722636690, 2073.2842783293, 18171.3303810435, 6057.5509651366, 4377.7564961406,
     7493.2057581627, 4392.0950500065, 5763.8853948030, 6252.0619261988],
    [2039, 372836.5061069000, 141336.4564682970, 2288.5875900305, 20058.3594054514, 6686.6064194344, 4832.3711774424,
     8271.3489350797, 4848.1987399140, 6362.4447080330, 6901.3166626291],
    [2040, 382763.8606326470, 143516.9441411690, 2521.3785739399, 22098.6593887010, 7366.7559117135, 5323.9112198305,
     9112.6955653085, 5341.3487332853, 7009.6210582433, 7603.3060919010],
    [2041, 392154.9678193790, 145533.1408824450, 2772.5756943007, 24300.2802240840, 8100.6829350289, 5854.3159679711,
     10020.5651364981, 5873.4907267611, 7707.9678447392, 8360.7998753602],
    [2042, 401001.2830503750, 147392.1511188970, 3043.0492550114, 26670.8497028497, 8890.9302715145, 6425.4230755742,
     10998.1030765348, 6446.4683929558, 8459.9045774662, 9176.4224451342],
    [2043, 409301.0527323390, 149101.7388876630, 3333.5995419306, 29217.3819421089, 9739.8361303705, 7038.9223526925,
     12048.2017560718, 7061.9770765908, 9267.6561109792, 10052.5870914784],
    [2044, 417058.6196610520, 150670.1115351290, 3644.9324383582, 31946.0636663699, 10649.4629031902, 7696.3042776145,
     13173.4123586899, 7721.5121377480, 10133.1848536596, 10991.4224304013],
    [2045, 424283.6490403780, 152105.7290993440, 3977.6328020099, 34862.0208696338, 11621.5193789975, 8398.8037821293,
     14375.8486607037, 8426.3125530136, 11058.1167537090, 11994.6921209887],
    [2046, 430990.3162896970, 153417.1404767920, 4332.1360751263, 37969.0699917880, 12657.2777970089, 9147.3403060443,
     15657.0844252192, 9177.3007736546, 12043.6623731317, 13063.7092546882],
    [2047, 437196.4925896250, 154612.8461420110, 4708.6988066945, 41269.4595601821, 13757.4877208904, 9942.4555546177,
     17018.0468643739, 9975.0202791873, 13090.5349373040, 14199.2474640263],
    [2048, 442922.9577194610, 155701.1861893830, 5107.3689881044, 44763.6101960558, 14922.2893679261, 10784.2508620569,
     18458.9094273005, 10819.5727357211, 14198.8678658806, 15401.4514687335],
    [2049, 448192.6628755570, 156690.2517737260, 5527.9573272010, 48449.8628455464, 16151.1296799130, 11672.3265364477,
     19978.9879796128, 11710.5571422229, 15368.1349125090, 16669.7504516342],
    [2050, 453030.0594348140, 157587.8175986250, 5970.0107919631, 52324.2469028787, 17442.6850252655, 12605.7259970190,
     21576.6451857149, 12647.0137848133, 16597.0766142796, 18002.7782786770],
    [2051, 457460.5034850030, 158401.2928907460, 6432.7899209007, 56380.2813470088, 18794.7949064055, 13582.8878648636,
     23249.2085046763, 13627.3761705693, 17883.6372129316, 19398.3050776367],
    [2052, 461509.7406628950, 159137.6882560350, 6915.2514966463, 60608.8228840608, 20204.4113368905, 14601.6093780853,
     24992.9075696123, 14649.4343228446, 19224.9164861409, 20853.1849897169],
    [2053, 465203.4715563390, 159803.5958948020, 7416.0381854680, 64997.9751426897, 21667.5685709984, 15659.0245155487,
     26802.8367431042, 15710.3128333668, 20617.1409445916, 22363.3249271367],
    [2054, 468566.9946562870, 160405.1808178660, 7933.4766346803, 69533.0719988084, 23179.3775448988, 16751.5999795451,
     28672.9482409143, 16806.4668317465, 22055.6585426355, 23923.6788358050],
    [2055, 471624.9215249320, 160948.1809229050, 8465.5852752095, 74196.7459612884, 24734.0486735452, 17875.1516709736,
     30596.0803317987, 17933.6985146188, 23534.9603700076, 25528.2712242326],
    [2056, 474400.9573608990, 161437.9140334640, 9010.0926921875, 78969.0891812978, 26324.9455243607, 19024.8834789982,
     32564.0237319918, 19087.1960623494, 25048.7317234521, 27170.2525607064],
    [2057, 476917.7393500300, 161879.2902536000, 9564.4669117418, 83827.9101367969, 27944.6703849639, 20195.4491203400,
     34567.6274526973, 20261.5956808703, 26589.9335261875, 28841.9875886372],
    [2058, 479196.7249433800, 162276.8282354370, 10125.9553338544, 88749.0836246704, 29585.1809357033, 21381.0364578334,
     36596.9431243071, 21451.0661964062, 28150.9133442440, 30535.1757455071],
    [2059, 481258.1223631550, 162634.6741858870, 10691.6343633977, 93706.9857526622, 31237.9352575222, 22575.4722967573,
     38641.4043714941, 22649.4141950473, 29723.5433644546, 32241.0008270087],
    [2060, 483120.8560791190, 162956.6226472710, 11258.4671127333, 98674.9996746467, 32894.0604226518, 23772.3442243390,
     40690.0353603226, 23850.2062613164, 31299.3808119965, 33950.3049912689]]

# Bioplastics "S Curve Adoption"!A129:K176
bass_diffusion_adoption_regions_NaN_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa",
     "Latin America", "China", "India", "EU", "USA"],
    [2014, 1.6700000000000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [2015, 2.7281030228136, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2016, 3.8937501931531, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2017, 5.1775339443944, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2018, 6.5910169547469, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2019, 8.1468051537722, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2020, 9.8586226570820, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    [2021, 11.7413877525030, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2022, 13.8112887881378, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2023, 16.0858584886745, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2024, 18.5840448456170, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2025, 21.3262762851648, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2026, 24.3345183109439, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2027, 27.6323182465546, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2028, 31.2448340671007, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2029, 35.1988426162818, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2030, 39.5227217693669, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2031, 44.2464003438062, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2032, 49.4012688102934, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2033, 55.0200431625830, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2034, 61.1365737244331, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2035, 67.7855902841905, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2036, 75.0023748479947, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2037, 82.8223536063427, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2038, 91.2806005475590, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2039, 100.4112466690280, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2040, 110.2467910792270, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2041, 120.8173135861020, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2042, 132.1495927354960, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2043, 144.2661387475320, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2044, 157.1841573647330, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2045, 170.9144681218860, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2046, 185.4604086748680, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2047, 200.8167651122010, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2048, 216.9687759655340, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2049, 233.8912641120170, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2050, 251.5479549770560, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2051, 269.8910404127560, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2052, 288.8610444339210, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2053, 308.3870389526580, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2054, 328.3872444620200, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2055, 348.7700325075650, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2056, 369.4353246122960, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2057, 390.2763575934720, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2058, 411.1817599989390, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2059, 432.0378611266350, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],

    [2060, 452.7311352662340, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
     np.nan]]

# Bioplastics "S Curve Adoption"!A129:K176
bass_diffusion_base_year_2018_list = [
    ["Year", "World", "OECD90", "Eastern Europe", "Asia (Sans Japan)", "Middle East and Africa",
     "Latin America", "China", "India", "EU", "USA"],
    [2014, -2.099620134] + [np.nan] * 9,
    [2015, 2.800368639] + [np.nan] * 9,
    [2016, 9.27846538] + [np.nan] * 9,
    [2017, 17.82626281] + [np.nan] * 9,
    [2018, 29.07618307] + [0.0] * 9,
    [2019, 40.32610334] + [np.nan] * 9,
    [2020, 54.25331424] + [np.nan] * 9,
    [2021, 71.4605658] + [np.nan] * 9,
    [2022, 92.66779254] + [np.nan] * 9,
    [2023, 118.7249017] + [np.nan] * 9,
    [2024, 150.6201913] + [np.nan] * 9,
    [2025, 189.4803886] + [np.nan] * 9,
    [2026, 236.5566624] + [np.nan] * 9,
    [2027, 293.189223] + [np.nan] * 9,
    [2028, 360.7417636] + [np.nan] * 9,
    [2029, 440.4968967] + [np.nan] * 9,
    [2030, 533.5063029] + [np.nan] * 9,
    [2031, 640.3962668] + [np.nan] * 9,
    [2032, 761.1420893] + [np.nan] * 9,
    [2033, 894.8433776] + [np.nan] * 9,
    [2034, 1039.552708] + [np.nan] * 9,
    [2035, 1192.223938] + [np.nan] * 9,
    [2036, 1348.841071] + [np.nan] * 9,
    [2037, 1504.753954] + [np.nan] * 9,
    [2038, 1655.185401] + [np.nan] * 9,
    [2039, 1795.807121] + [np.nan] * 9,
    [2040, 1923.243578] + [np.nan] * 9,
    [2041, 2035.37981] + [np.nan] * 9,
    [2042, 2131.417246] + [np.nan] * 9,
    [2043, 2211.705766] + [np.nan] * 9,
    [2044, 2277.43914] + [np.nan] * 9,
    [2045, 2330.314353] + [np.nan] * 9,
    [2046, 2372.231348] + [np.nan] * 9,
    [2047, 2405.071373] + [np.nan] * 9,
    [2048, 2430.559166] + [np.nan] * 9,
    [2049, 2450.194899] + [np.nan] * 9,
    [2050, 2465.235297] + [np.nan] * 9,
    [2051, 2476.704638] + [np.nan] * 9,
    [2052, 2485.420971] + [np.nan] * 9,
    [2053, 2492.027847] + [np.nan] * 9,
    [2054, 2497.025847] + [np.nan] * 9,
    [2055, 2500.801068] + [np.nan] * 9,
    [2056, 2503.649417] + [np.nan] * 9,
    [2057, 2505.796604] + [np.nan] * 9,
    [2058, 2507.414177] + [np.nan] * 9,
    [2059, 2508.632172] + [np.nan] * 9,
    [2060, 2509.548955] + [np.nan] * 9]