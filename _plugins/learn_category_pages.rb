# frozen_string_literal: true

module Jekyll
  class LearnCategoryPagesGenerator < Generator
    safe true
    priority :low

    LANGUAGES = %w[ko en ja zh-cn zh-tw].freeze

    def generate(site)
      categories = site.data.fetch("learn_categories", {})
      LANGUAGES.each do |language|
        index_key = language == "ko" ? "courses" : "courses-#{language}"
        next unless site.data.fetch("learn", {}).key?(index_key)

        categories.each_key do |category|
          prefix = language == "ko" ? "learn" : "learn/#{language}"
          page = PageWithoutAFile.new(
            site,
            site.source,
            "#{prefix}/category/#{category}",
            "index.html"
          )
          page.content = ""
          page.data = {
            "layout" => "learn-catalogue",
            "title" => "Learn",
            "lang" => language,
            "learn_index_key" => index_key,
            "learn_category" => category,
            "permalink" => "/#{prefix}/category/#{category}/",
            "no_ads" => true,
            "ref" => "learn-category:#{category}",
            "translations" => LANGUAGES.map do |translated_language|
              translated_prefix = translated_language == "ko" ? "learn" : "learn/#{translated_language}"
              {
                "lang" => translated_language,
                "url" => "/#{translated_prefix}/category/#{category}/"
              }
            end
          }
          site.pages << page
        end
      end
    end
  end
end
