def test_click_women_sale_image(sale_page):
    sale_page.open_page()
    sale_page.click_women_category()
    sale_page.verify_page_title("Women Sale")


def test_click_men_sale_image(sale_page):
    sale_page.open_page()
    sale_page.click_men_category()
    sale_page.verify_page_title("Men Sale")


def test_training_video_displayed(sale_page):
    sale_page.open_page()
    sale_page.hover_on_training_menu()
    sale_page.select_training_option()
    sale_page.verify_training_video_is_displayed()
