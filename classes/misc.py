class Misc:
    def __init__(self):
        self.banner = \
"""
::::::::::: :::::::::: ::::::::  :::            :::     :::::::::  :::            :::   :::   ::: 
    :+:     :+:       :+:    :+: :+:          :+: :+:   :+:    :+: :+:          :+: :+: :+:   :+: 
    +:+     +:+       +:+        +:+         +:+   +:+  +:+    +:+ +:+         +:+   +:+ +:+ +:+  
    +#+     +#++:++#  +#++:++#++ +#+        +#++:++#++: +#++:++#+  +#+        +#++:++#++: +#++:   
    +#+     +#+              +#+ +#+        +#+     +#+ +#+        +#+        +#+     +#+  +#+    
    #+#     #+#       #+#    #+# #+#        #+#     #+# #+#        #+#        #+#     #+#  #+#    
    ###     ########## ########  ########## ###     ### ###        ########## ###     ###  ###    
                                            by luwzko                                            """

        self.setts_menu = [
            "Settings are easy to use and based on YAML syntax.",
            "To add new games, edit settings.yaml file.",
            "Syntax in settings.yaml is: 'id':['game_name', 'game_exec_path', 'game_desc'].",
            "To add a game with ID 3, increment the previous game's ID.",
            "Then add new game details as: '3':['Example Game name', 'example.exe', 'example description']"
        ]
        self.about_menu = [
            "A game launcher designed with Python and equipped with a curses GUI.",
            "The central theme of this masterpiece is retro gaming fun.",
            "It was created during the 2022/2023 school year.",
            "It is still undergoing continuous development.",
            "With exciting new updates on the horizon!",
            "So sit back, relax, and enjoy the ride!! :)"
        ]
        self.star = "╪"
