You can use tests only on Linux

For running test you need to:

1. Create file (.env) in the project directory
2. In the file write:

    user_name = ""
    user_password = ""

    user_id_walmart = ""
    user_secret_walmart = ""

    user_id_ebay = ""
    user_secret_ebay = ""

    user_id_amazon = ""
    user_secret_amazon = ""
    two_step_auth = ""

In the user_name and user_password you need to write credentials for Magento.
In the user_id_walmart and user_secret_walmart you need to write credentials for Walmart.
In the user_id_ebay and user_secret_ebay you need to write credentials for eBay.
In the user_id_amazon and user_secret_amazon you need to write credentials for Amazon.
In the two_step_auth you need to write code for the two step verification which is required during amazon account on-boarding

3. In file m2/config/local_config.py change VM_IP on your Virtual Machine IP (10.0.30.XXX)
4. Install python 3.6 or higher.
5. Install required packages with the command: pip install -r requirements.txt
6. Open Terminal and go to the autotests directory.
7. Run autotest with the command: pytest --tb=short -v -m ebay_policy -W ignore(
    --tb=short - это более короткий вывод информации, если вдруг тест упал
    -m [после него должно идти название маркера тех автотестов, которые хотите запустить]
                                                            - запускает тесты с определенной маркировкой
    -W ignore - иногда pytest может кидать стандартные ворнинги, которые никак не влияют на работу.
                                                             флаг -W ignore убирает эти ворнинги из вывода
    -v (verbose). то есть подробный - используется для отображения % пройденных тестов и
                                                              вывода информации о Passed or Failed)

    Список других полезных команд для манипуляции выводом: https://gist.github.com/amatellanes/12136508b816469678c2


