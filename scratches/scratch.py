area = Area(
        "Grid",
        [
            # Area(
                "",
            #     [
            #         Area("prodiucer ",
            #              [
            #                  Area("Load 1 L13", strategy=LoadProfileExternalStrategy(
            #                      daily_load_profile=os.path.join(current_dir,
            #                                                      "resources/CHR27 Family both at work, 2 children HH1.csv"),
            #                      initial_buying_rate=11,
            #                      use_market_maker_rate=True),
            #                       ),
            #                  Area("PV 1 (4kW)", strategy=PVUserProfileExternalStrategy(
            #                      power_profile=os.path.join(current_dir, "resources/Berlin_pv.csv"),
            #                      panel_count=4,
            #                      initial_selling_rate=30,
            #                      final_selling_rate=11),
            #                       ),
            #              ]),