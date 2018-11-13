""" https://docs.google.com/spreadsheets/d/1MsDWgYDIcPE_5nX6pRbea-hW9JQjYikfCDWk16l5V-8/pubhtml# """

from collections import defaultdict

_BLESSED_SUNFRUIT_ADDITIONAL_STRENGTH = 10
_DENSE_SHARPENING_STONE_ADDITIONAL_DAMAGE = (8, 8)
_ELEMENTAL_SHARPENING_STONE_ADDITIONAL_CRIT = 2
_ELIXIR_OF_THE_MONGOOSE_ADDITIONAL_AGILITY = 25
_ELIXIR_OF_THE_MONGOOSE_ADDITIONAL_CRIT = 2
_JUJU_MIGHT_ADDITIONAL_AP = 40
_JUJU_POWER_ADDITIONAL_STRENGTH = 30
_ROIDS_ADDITIONAL_STRENGTH = 25

CONSUMABLE_STATS = defaultdict(int, {
    'agi': _ELIXIR_OF_THE_MONGOOSE_ADDITIONAL_AGILITY,
    'ap': _JUJU_MIGHT_ADDITIONAL_AP,
    'crit': _ELEMENTAL_SHARPENING_STONE_ADDITIONAL_CRIT + _ELEMENTAL_SHARPENING_STONE_ADDITIONAL_CRIT + _ELIXIR_OF_THE_MONGOOSE_ADDITIONAL_CRIT,
    # 'damage_range_main_hand': _DENSE_SHARPENING_STONE_ADDITIONAL_DAMAGE,
    'str': _BLESSED_SUNFRUIT_ADDITIONAL_STRENGTH + _JUJU_POWER_ADDITIONAL_STRENGTH + _ROIDS_ADDITIONAL_STRENGTH
})
CONSUMABLE_ON_USE_EFFECTS = set()