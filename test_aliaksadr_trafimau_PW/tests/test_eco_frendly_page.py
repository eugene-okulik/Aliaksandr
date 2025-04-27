def test_select_option(category_page):
    category_page.open_page()
    category_page.select_subcategory()
    category_page.verify_image_is_displayed()


def test_select_sort_price(category_page):
    category_page.open_page()
    category_page.sort_products_by_price()
    category_page.verify_selected_sorting_option()


def test_check_training_option(category_page):
    category_page.open_page()
    category_page.select_training_element()
    category_page.select_video_option()
    category_page.verify_training_video_message_is_displayed()
