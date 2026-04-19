source "https://rubygems.org"

# This is the same Jekyll version GitHub Pages runs. Using github-pages
# gem keeps everything in sync with what GitHub builds for you.
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end

# Needed on Windows / some Ruby versions
gem "webrick", "~> 1.8"

# Ruby 3.4+ removed these from the standard library; Jekyll still expects them
gem "csv"
gem "base64"
gem "logger"
gem "bigdecimal"

# Windows and JRuby don't include zoneinfo files, so bundle tzinfo-data
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
  gem "wdm", "~> 0.2.0"
end
