require 'awesome_print'

f = File.open('putative-standardized-symptoms.txt') or die 'Could not find file'

symptoms = f.each_line{|line|}
ap symptoms