"""Test solution classes."""
import dataclasses
import json
from . import factory
from model import scenario
from model import advanced_controls as ac

def test_all_solutions():
    result = factory.all_solutions()
    assert 'solarpvutil' in result
    assert 'silvopasture' in result

def test_list_scenarios():
    result = factory.list_scenarios('silvopasture')
    assert len(result) > 0

def test_load_PDS_scenario():
    result = factory.load_scenario('peatlands','PDS2')
    assert result and isinstance(result, scenario.Scenario)

def test_load_named_scenario():
    scenarios = factory.list_scenarios('geothermal')
    result = factory.load_scenario('geothermal', scenarios[0])
    assert result and isinstance(result, scenario.Scenario)

def test_load_custom_scenario_by_copying():
    onescenario = factory.load_scenario('hybridcars')
    
    # Make a new Advanced Controls by dumping one and tweaking it
    oneac = dataclasses.asdict(onescenario.ac)
    oneac['name'] = "Change the Name"
    twoac = ac.AdvancedControls(**oneac)

    result = factory.load_scenario('hybridcars',twoac)
    assert result.scenario == "Change the Name"


def test_load_custom_scenario_from_dict():
    adict = json.loads(biochar_scenario_json)
    result = factory.load_scenario("biochar",adict)
    assert result.ac.conv_fuel_emissions_factor == 0
    assert result.tm.ref_tam_per_region() is not None

biochar_scenario_json="""
{
    "name": "PDS-8p2050-Plausible-CustomPDS-Avg-Jan2020",
    "solution_category": "reduction",
    "vmas": "VMAs",
    "description": "This is updated results with new data.",
    "report_start_year": 2020,
    "report_end_year": 2050,
    "conv_2014_cost": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_first_cost_efficiency_rate": 0.0,
    "conv_lifetime_capacity": {
        "value": 1.0,
        "statistic": ""
    },
    "conv_avg_annual_use": {
        "value": 1.0,
        "statistic": ""
    },
    "conv_var_oper_cost_per_funit": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_fixed_oper_cost_per_iunit": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_fuel_cost_per_funit": 0.0,
    "pds_2014_cost": {
        "value": 21639272.7272727,
        "statistic": "mean"
    },
    "ref_2014_cost": {
        "value": 21639272.7272727,
        "statistic": "mean"
    },
    "soln_first_cost_efficiency_rate": 0.0,
    "soln_first_cost_below_conv": true,
    "soln_lifetime_capacity": {
        "value": 410116.363636364,
        "statistic": "mean"
    },
    "soln_avg_annual_use": {
        "value": 20505.8181818182,
        "statistic": "mean"
    },
    "soln_var_oper_cost_per_funit": {
        "value": 193.920714285714,
        "statistic": "mean"
    },
    "soln_fixed_oper_cost_per_iunit": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_fuel_cost_per_funit": 0.0,
    "npv_discount_rate": 0.02,
    "conv_annual_energy_used": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_energy_efficiency_factor": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_annual_energy_used": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_fuel_consumed_per_funit": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_fuel_efficiency_factor": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_fuel_emissions_factor": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_fuel_emissions_factor": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_emissions_per_funit": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_emissions_per_funit": {
        "value": -0.958331730769231,
        "statistic": "mean"
    },
    "conv_indirect_co2_per_unit": {
        "value": 0.0,
        "statistic": ""
    },
    "soln_indirect_co2_per_iunit": {
        "value": 0.0,
        "statistic": ""
    },
    "conv_indirect_co2_is_iunits": true,
    "ch4_co2_per_funit": {
        "value": 0.0,
        "statistic": ""
    },
    "ch4_is_co2eq": false,
    "n2o_co2_per_funit": {
        "value": 0.0,
        "statistic": ""
    },
    "n2o_is_co2eq": false,
    "co2eq_conversion_source": "AR5 with feedback",
    "emissions_use_co2eq": true,
    "emissions_grid_source": "Meta-Analysis",
    "emissions_grid_range": "Mean",
    "source_until_2014": "ALL SOURCES",
    "ref_source_post_2014": "ALL SOURCES",
    "pds_source_post_2014": "ALL SOURCES",
    "ref_base_adoption": {
        "World": 7457.0,
        "OECD90": 0.0,
        "Eastern Europe": 0.0,
        "Asia (Sans Japan)": 0.0,
        "Middle East and Africa": 0.0,
        "Latin America": 0.0,
        "China": 0.0,
        "India": 0.0,
        "EU": 0.0,
        "USA": 0.0
    },
    "soln_pds_adoption_basis": "Fully Customized PDS",
    "soln_pds_adoption_regional_data": false,
    "pds_adoption_final_percentage": [
        [
            "World",
            0.0
        ],
        [
            "OECD90",
            0.0
        ],
        [
            "Eastern Europe",
            0.0
        ],
        [
            "Asia (Sans Japan)",
            0.0
        ],
        [
            "Middle East and Africa",
            0.0
        ],
        [
            "Latin America",
            0.0
        ],
        [
            "China",
            0.0
        ],
        [
            "India",
            0.0
        ],
        [
            "EU",
            0.0
        ],
        [
            "USA",
            0.0
        ]
    ],
    "soln_pds_adoption_custom_name": "Average of All Custom PDS Scenarios",
    "soln_ref_adoption_basis": "Custom",
    "soln_ref_adoption_custom_name": "Average of All Custom REF Scenarios",
    "soln_ref_adoption_regional_data": false
}"""
