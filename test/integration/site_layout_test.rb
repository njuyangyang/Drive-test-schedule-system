require 'test_helper'

class SiteLayoutTest < ActionDispatch::IntegrationTest

  test "layout links" do
    get root_path
    assert_template 'static_pages/home'
    assert_select "a[href=?]", root_path, count: 2
    assert_select "a[href=?]", static_pages_help_path
    assert_select "a[href=?]", static_pages_about_path
    assert_select "a[href=?]", static_pages_contact_path
  end
end