module Jekyll
  class Page
    def yaml_file?
      %w(.yaml .yml).include?(ext)
    end
  end
end
