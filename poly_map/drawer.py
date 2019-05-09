#!/usr/bin/env python
import random
import numpy as np
import cv2
image = cv2.imread("../gtasa-geographic-1.0.jpg")

grove_colors = (34, 139, 34)
ballas_colors = (128, 0, 128)
vagos_colors = (0, 215, 255)
aztecas_colors = (255, 144, 30)
mcb_colors = (153, 136, 119)
rgt_colors = (0, 0, 204)
dnb_colors = (11, 134, 184)
rifas_colors = (185, 185, 0)
leone_colors = (0, 0, 139)
forelli_colors = (112, 25, 25)
sindacco_colors = (40, 40, 40)
black = (0, 0, 0)
ls_colors = (grove_colors, ballas_colors, vagos_colors, aztecas_colors)
lv_colors = (leone_colors, forelli_colors, sindacco_colors)
sf_colors = (mcb_colors, rgt_colors, dnb_colors, rifas_colors)

ganton_coords = [(5225, 4631), (5225, 4849), (5630, 4849), (5630, 4631), (5225, 4631)]
idlewood_coords = [(4814, 4850), (4815, 4452), (5121, 4452), (5121, 4497), (5220, 4497), (5220, 4850), (4814, 4850)]
jefferson_coords = [(4998, 4447), (4998, 4352), (5058, 4352), (5058, 4128), (5183, 4128), (5183, 4156), (5279, 4156), (5278, 4369), (5263, 4369), (5264, 4492), (5126, 4492), (5126, 4447), (4998, 4447)]
east_los_santos_coords = [(5225, 4626), (5225, 4497), (5269, 4497), (5268, 4374), (5283, 4374), (5284, 4137), (5579, 4137), (5578, 4457), (5629, 4457), (5629, 4626), (5225, 4626)]
los_flores_coords = [(5584, 4137), (5745, 4138), (5745, 4390), (5630, 4390), (5630, 4452), (5583, 4452), (5584, 4137)]
east_beach_coords = [(5750, 4123), (5955, 4123), (5955, 4850), (5635, 4849), (5635, 4395), (5750, 4395), (5750, 4123)]
las_colinas_coords = [(5955, 4118), (5955, 3947), (5279, 3947), (5279, 3936), (5124, 3936), (5124, 3922), (4996, 3922), (4996, 4098), (5058, 4098), (5058, 4123), (5188, 4123), (5188, 4151), (5279, 4151), (5279, 4132), (5745, 4133), (5745, 4118), (5955, 4118)]
playa_del_seville_coords = [(5706, 4855), (5957, 4855), (5957, 5123), (5706, 5123), (5706, 4855)]
willowfield_coords = [(5701, 4854), (5701, 5057), (5322, 5056), (5322, 5093), (5199, 5093), (5200, 5232), (5091, 5232), (5091, 5177), (4972, 5177), (4972, 4855), (5701, 4854)]
glen_park_coords = [(4993, 4447), (4814, 4447), (4814, 3975), (4991, 3975), (4991, 4103), (5053, 4103), (5053, 4347), (4993, 4347), (4993, 4447)]
north_ocean_docks_coords = [(5091, 5237), (5092, 5392), (5203, 5392), (5203, 5415), (5322, 5415), (5322, 5300), (5957, 5300), (5957, 5128), (5701, 5128), (5701, 5062), (5327, 5061), (5327, 5098), (5204, 5098), (5204, 5237), (5091, 5237)]
south_ocean_docks_coords = [(5375, 5695), (5807, 5695), (5807, 5332), (5375, 5332), (5375, 5695)]
los_santos_airport_coords = [(5198, 5397), (5198, 5728), (4384, 5728), (4384, 5392), (4251, 5392), (4251, 5181), (5086, 5182), (5087, 5397), (5198, 5397)]
corona_coords = [(4967, 5176), (4694, 5177), (4694, 4974), (4815, 4974), (4815, 4855), (4967, 4855), (4967, 5176)]
unity_station_coords = [(4694, 4969), (4694, 4844), (4809, 4845), (4809, 4855), (4812, 4855), (4812, 4969), (4694, 4969)]
little_mexico_coords = [(4810, 4840), (4703, 4840), (4703, 4724), (4760, 4724), (4760, 4579), (4810, 4579), (4810, 4840)]
verdant_bluffs_coords = [(4247, 5486), (3932, 5486), (3933, 5009), (4076, 5009), (4076, 4845), (4689, 4845), (4689, 5176), (4246, 5176), (4247, 5486)]
commerce_coords = [(4698, 4839), (4326, 4840), (4325, 4579), (4372, 4579), (4372, 4386), (4461, 4386), (4461, 4432), (4809, 4433), (4810, 4574), (4755, 4574), (4755, 4719), (4698, 4719), (4698, 4839)]
downtown_los_santos_coords = [(4810, 4428), (4466, 4427), (4466, 4381), (4372, 4381), (4372, 4132), (4380, 4132), (4380, 4028), (4393, 4028), (4393, 3928), (4461, 3928), (4461, 4152), (4810, 4152)]
conference_center_coords = [(4321, 4840), (4321, 4724), (4048, 4725), (4048, 4802), (4075, 4802), (4075, 4840), (4321, 4840)]
verona_beach_coords = [(4320, 4719), (4320, 4579), (3853, 4580), (3853, 4807), (3649, 4807), (3649, 5171), (3928, 5171), (3928, 5004), (4070, 5004), (4070, 4807), (4043, 4807), (4043, 4721), (4320, 4719)]
market_coords = [(4367, 4574), (4367, 4133), (3954, 4132), (3954, 4313), (3869, 4313), (3790, 4312), (3790, 4413), (3790, 4418), (3649, 4418), (3649, 4802), (3848, 4802), (3848, 4575), (4367, 4574)]
vinewood_coords = [(3785, 4413), (3649, 4413), (3649, 4120), (3790, 4120), (3790, 3957), (3949, 3957), (3949, 4308), (3784, 4307), (3785, 4413)]
temple_coords = [(3954, 4127), (3955, 3940), (4099, 3940), (4099, 3913), (4355, 3912), (4355, 3928), (4388, 3928), (4388, 4023), (4377, 4023), (4377, 4128), (3954, 4127)]
mulholland_intersection_coords = [(4466, 4147), (4466, 3771), (4810, 3770), (4809, 4147), (4466, 4147)]
richman_coords = [(3074, 4401), (3074, 4010), (3323, 4010), (3323, 3676), (3698, 3676), (3698, 3765), (3684, 3765), (3684, 3862), (3766, 3862), (3766, 3957), (3785, 3957), (3785, 4115), (3644, 4115), (3644, 4232), (3464, 4231), (3464, 4290), (3332, 4290), (3332, 4367), (3222, 4367), (3222, 4401), (3074, 4401)]
rodeo_coords = [(3645, 4682), (3074, 4682), (3074, 4406), (3227, 4406), (3227, 4372), (3337, 4372), (3337, 4295), (3469, 4295), (3469, 4237), (3644, 4237), (3645, 4682)]
santa_marina_beach_coords = [(3074, 4687), (3644, 4687), (3644, 5171), (3074, 5171), (3074, 4687)]
mulholland_coords = [(3771, 3952), (3771, 3857), (3689, 3857), (3689, 3770), (3739, 3770), (3739, 3676), (3863, 3676), (3863, 3602), (4154, 3602), (4154, 3672), (4140, 3672), (4140, 3770), (4271, 3770), (4271, 3454), (4283, 3454), (4283, 3292), (4639, 3292), (4639, 3454), (4665, 3454), (4665, 3766), (4461, 3766), (4461, 3923), (4360, 3923), (4360, 3907), (4094, 3908), (4094, 3935), (3950, 3935), (3950, 3952), (3771, 3952)]
ls_zones = [
	ganton_coords,
	idlewood_coords,
	jefferson_coords,
	east_los_santos_coords,
	los_flores_coords,
	east_beach_coords,
	las_colinas_coords,
	playa_del_seville_coords,
	willowfield_coords,
	glen_park_coords,
	north_ocean_docks_coords,
	south_ocean_docks_coords,
	los_santos_airport_coords,
	corona_coords,
	unity_station_coords,
	little_mexico_coords,
	verdant_bluffs_coords,
	commerce_coords,
	downtown_los_santos_coords,
	conference_center_coords,
	verona_beach_coords,
	market_coords,
	vinewood_coords,
	temple_coords,
	mulholland_intersection_coords,
	richman_coords,
	rodeo_coords,
	santa_marina_beach_coords,
	mulholland_coords
	]
last_dime_hotel_coords = [(4825, 2401), (4825, 2179), (4995, 2179), (4995, 2401), (4825, 2401)]
randolph_industrial_state_coords = [(4561, 2179), (4561, 2401), (4820, 2401), (4820, 2179), (4561, 2179)]
blackfield_chapel_coords = [(4556, 2401), (4556, 2179), (4377, 2179), (4377, 2206), (4327, 2206), (4327, 2401), (4556, 2401)]
rockshore_west_coords = [(5000, 2401), (5000, 2179), (5374, 2179), (5374, 2214), (5535, 2214), (5535, 2401), (5000, 2401)]
rockshore_east_coords = [(5540, 2321), (5539, 2058), (5900, 2059), (5900, 2321), (5540, 2321)]
blackfield_intersection_coords = [(4169, 2201), (4169, 1958), (4199, 1958), (4199, 1838), (4275, 1839), (4275, 1914), (4313, 1914), (4313, 1958), (4372, 1958), (4372, 2082), (4455, 2082), (4455, 2174), (4372, 2174), (4372, 2201), (4169, 2201)]
linden_side_coords = [(5752, 2054), (5751, 1803), (5921, 1803), (5921, 2054), (5752, 2054)]
linden_station_coords = [(5921, 1798), (5751, 1798), (5751, 1453), (5921, 1453), (5921, 1798)]
sobell_rail_yards_coords = [(5921, 1448), (5751, 1448), (5751, 1064), (5921, 1064), (5921, 1448)]
blackfield_college_coords = [(3966, 2067), (3966, 1798), (4195, 1798), (4194, 1953), (4164, 1953), (4164, 2067), (3966, 2067)]
blackfield_coords = [(3966, 1793), (3966, 1275), (4194, 1276), (4194, 1793), (3966, 1793)]
white_wood_estates_coords = [(3885, 1271), (3885, 1271), (3885, 494), (4095, 494), (4095, 758), (4194, 758), (4194, 1271), (3885, 1271)]
creek_coords = [(5919, 1059), (5752, 1059), (5752, 332), (5919, 332), (5919, 1059)]
pilson_intersection_coords = [(4100, 753), (4100, 494), (4374, 494), (4374, 753), (4100, 753)]
prickle_pine_coords = [(4119, 489), (4119, 279), (4537, 279), (4537, 138), (4936, 138), (4936, 140), (5119, 140), (5118, 372), (4935, 372), (4935, 443), (4850, 443), (4850, 413), (4531, 413), (4531, 489), (4119, 489)]
yellow_bell_golf_club_coords = [(4532, 274), (4119, 274), (4119, 138), (4532, 138), (4532, 274)]
kacc_military_fuels_coords = [(5747, 371), (5501, 370), (5500, 140), (5747, 140), (5747, 371)]
spiny_bed_coords = [(5495, 333), (5124, 333), (5124, 140), (5495, 140), (5495, 333)]
come_a_lot_coords = [(5620, 2053), (5090, 2054), (5090, 1799), (5620, 1799), (5620, 2053)]
four_dragons_casino_coords = [(5025, 2133), (4819, 2133), (4819, 1919), (5025, 1919), (5025, 2133)]
lva_freight_depot_coords = [(4774, 2133), (4460, 2133), (4460, 2077), (4377, 2077), (4377, 1953), (4318, 1953), (4318, 1909), (4280, 1909), (4280, 1834), (4238, 1834), (4238, 1798), (4454, 1798), (4454, 1859), (4774, 1859), (4774, 2133)]
las_venturas_airport_coords = [(4775, 1854), (4459, 1854), (4459, 1793), (4239, 1793), (4239, 1119), (4774, 1119), (4775, 1854)]
camel_toe_coords = [(5638, 1794), (5090, 1794), (5090, 1619), (5638, 1619), (5638, 1794)]
pink_swan_coords = [(5025, 1914), (4819, 1914), (4819, 1719), (5025, 1719), (5025, 1914)]
the_highway_roller_coords = [(5025, 1714), (4819, 1714), (4819, 1532), (5025, 1532), (5025, 1714)]
royal_casino_coords = [(5435, 1614), (5090, 1614), (5090, 1459), (5435, 1459), (5435, 1614)]
pilgrim_coords = [(5440, 1614), (5440, 1219), (5683, 1218), (5683, 1614), (5440, 1614)]
caligula_palace_coords = [(5435, 1454), (5090, 1454), (5090, 1299), (5140, 1299), (5140, 1219), (5435, 1218), (5435, 1454)]
pirates_in_mens_pants_coords = [(5025, 1527), (4819, 1527), (4819, 1299), (5025, 1299), (5025, 1527)]
clowns_pocket_coords = [(5435, 1213), (5165, 1213), (5165, 1118), (5434, 1118), (5435, 1213)]
starfish_casino_coords = [(5683, 1213), (5440, 1214), (5440, 1113), (5165, 1113), (5165, 989), (5683, 989), (5683, 1213)]
the_visage_coords = [(5024, 1294), (4819, 1294), (4819, 990), (5103, 990), (5103, 1133), (5024, 1133), (5024, 1294)]
redsands_west_coords = [(4239, 1114), (4239, 860), (4300, 860), (4300, 758), (4379, 758), (4379, 569), (4701, 569), (4701, 659), (4775, 659), (4774, 1114), (4239, 1114)]
old_venturas_strip_coords = [(5683, 984), (5165, 984), (5165, 800), (5683, 800), (5683, 984)]
redsands_east_coords = [(5103, 985), (4819, 985), (4819, 660), (4851, 660), (4850, 524), (5009, 523), (5009, 799), (5103, 799), (5103, 985)]
emerald_isle_coords = [(5014, 794), (5013, 494), (5235, 494), (5235, 795), (5014, 794)]
roca_escalante_coords = [(5622, 795), (5240, 794), (5240, 460), (5533, 460), (5533, 560), (5622, 560), (5622, 795)]

lv_zones = [
	last_dime_hotel_coords,
	randolph_industrial_state_coords,
	blackfield_chapel_coords,
	rockshore_west_coords,
	rockshore_east_coords,
	blackfield_intersection_coords,
	linden_side_coords,
	linden_station_coords,
	sobell_rail_yards_coords,
	blackfield_college_coords,
	blackfield_coords,
	white_wood_estates_coords,
	creek_coords,
	pilson_intersection_coords,
	prickle_pine_coords,
	yellow_bell_golf_club_coords,
	kacc_military_fuels_coords,
	spiny_bed_coords,
	come_a_lot_coords,
	four_dragons_casino_coords,
	lva_freight_depot_coords,
	las_venturas_airport_coords,
	camel_toe_coords,
	pink_swan_coords,
	the_highway_roller_coords,
	royal_casino_coords,
	pilgrim_coords,
	caligula_palace_coords,
	pirates_in_mens_pants_coords,
	clowns_pocket_coords,
	starfish_casino_coords,
	the_visage_coords,
	redsands_west_coords,
	old_venturas_strip_coords,
	redsands_east_coords,
	emerald_isle_coords,
	roca_escalante_coords
	]
chinatown_coords = [(727, 2419), (727, 2257), (919, 2257), (919, 2419), (727, 2419)]
downtown_coords = [(924, 2257), (1019, 2257), (1019, 1728), (1376, 1727), (1376, 1826), (1416, 1826), (1416, 1977), (1498, 1977), (1498, 2419), (1203, 2419), (1203, 2732), (1009, 2732), (1009, 2418), (924, 2418), (924, 2257)]
juniper_hill_coords = [(722, 2418), (469, 2418), (469, 2033), (723, 2033), (722, 2418)]
kings_coords = [(1004, 2732), (590, 2732), (590, 2629), (749, 2629), (749, 2538), (673, 2538), (673, 2423), (1004, 2423), (1004, 2732)]
calton_heights_coords = [(728, 2252), (728, 1644), (1014, 1644), (1014, 2252), (728, 2252)]
esplanade_north_coords = [(469, 1639), (468, 1500), (1006, 1500), (1006, 1409), (1473, 1409), (1473, 1722), (1019, 1723), (1019, 1639), (469, 1639)]
esplanade_east_coords = [(1381, 1727), (1658, 1727), (1657, 2071), (1503, 2071), (1503, 1972), (1421, 1972), (1421, 1821), (1381, 1821), (1381, 1727)]
garver_bridge_coords = [(1502, 2301), (1503, 2076), (1662, 2076), (1662, 1944), (1788, 1944), (1788, 1823), (1910, 1823), (1909, 2047), (1784, 2047), (1784, 2169), (1657, 2169), (1657, 2301), (1502, 2301)]
kincide_bridge_coords = [(1503, 2419), (1503, 2306), (1662, 2306), (1662, 2174), (1789, 2174), (1789, 2052), (1914, 2052), (1914, 2015), (2036, 2015), (2036, 2142), (1910, 2142), (1910, 2276), (1784, 2276), (1784, 2420), (1503, 2419)]
easter_basin_coords = [(1208, 2424), (1207, 3048), (1497, 3048), (1497, 2747), (1754, 2747), (1754, 2423), (1208, 2424)]
juniper_hollow_coords = [(723, 2028), (469, 2028), (469, 1644), (723, 1644), (723, 2028)]
battery_point_coords = [(464, 1729), (260, 1729), (260, 1512), (464, 1511), (464, 1729)]
paradiso_coords = [(464, 2203), (260, 2203), (260, 1734), (464, 1734), (464, 2203)]
santa_flora_coords = [(463, 2539), (260, 2538), (260, 2208), (464, 2208), (463, 2539)]
palisades_coords = [(255, 1662), (7, 1662), (7, 2538), (255, 2538), (255, 1662)]
easter_bay_airport_coords = [(1759, 2423), (2050, 2423), (2050, 3048), (1865, 3048), (1864, 3728), (1208, 3728), (1208, 3053), (1502, 3053), (1502, 2752), (1759, 2752), (1759, 2423)]
foster_valley_coords = [(1203, 4248), (823, 4248), (823, 3428), (731, 3428), (732, 3326), (1203, 3327), (1203, 4248)]
missionary_hill_coords = [(818, 3809), (7, 3809), (7, 3433), (818, 3433), (818, 3809)]
doherty_coords = [(1203, 3322), (732, 3321), (731, 3224), (829, 3224), (829, 2737), (1202, 2737), (1203, 3322)]
avispa_country_club_coords = [(171, 3428), (351, 3428), (351, 3353), (640, 3353), (640, 3415), (727, 3415), (726, 3224), (643, 3224), (643, 3206), (606, 3206), (606, 3224), (171, 3224), (171, 3428)]
garcia_coords = [(824, 3219), (648, 3219), (648, 3201), (601, 3201), (601, 3219), (591, 3219), (591, 2737), (824, 2737), (824, 3219)]
queens_coords = [(586, 2942), (408, 2942), (409, 2544), (468, 2544), (468, 2423), (668, 2423), (668, 2543), (744, 2543), (744, 2624), (585, 2624), (586, 2942)]
hasbury_coords = [(586, 3219), (408, 3219), (408, 2947), (586, 2947), (586, 3219)]
city_hall_coords = [(404, 2720), (135, 2720), (135, 2543), (404, 2543), (404, 2720)]
ocean_flats_coords = [(403, 3219), (166, 3219), (166, 3428), (7, 3428), (7, 2543), (130, 2543), (130, 2725), (403, 2725), (403, 3219)]
sf_zones = [
	chinatown_coords,
	downtown_coords,
	juniper_hill_coords,
	kings_coords,
	calton_heights_coords,
	esplanade_north_coords,
	esplanade_east_coords,
	garver_bridge_coords,
	kincide_bridge_coords,
	easter_basin_coords,
	juniper_hollow_coords,
	battery_point_coords,
	paradiso_coords,
	santa_flora_coords,
	palisades_coords,
	easter_bay_airport_coords,
	foster_valley_coords,
	missionary_hill_coords,
	doherty_coords,
	avispa_country_club_coords,
	garcia_coords,
	queens_coords,
	hasbury_coords,
	city_hall_coords,
	ocean_flats_coords
	]
for i in ls_zones:
	cv2.fillPoly(image, [np.array(i)], random.choice(ls_colors))
	cv2.polylines(image, [np.array(i)], True, black, thickness=5)
for i in lv_zones:
	cv2.fillPoly(image, [np.array(i)], random.choice(lv_colors))
	cv2.polylines(image, [np.array(i)], True, black, thickness=5)
for i in sf_zones:
	cv2.fillPoly(image, [np.array(i)], random.choice(sf_colors))
	cv2.polylines(image, [np.array(i)], True, black, thickness=5)
cv2.namedWindow('test map', cv2.WINDOW_NORMAL)
cv2.imshow("test map", image)
cv2.waitKey(0)
cv2.imwrite('test_map.jpg', image)
# cv2.fillPoly(image, (np.array(ganton_coords)), random.choice(ls_colors))
