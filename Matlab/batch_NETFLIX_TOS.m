files = dir('../RAW/TOS/');

isd = {files.isdir};

fld = {files.folder};

fln = {files.name};


for i=1:length(files)
    
    if ~isd{i}

        subtitle_reader_NETFLIX_TOS([fld{i} '/' fln{i}],2)
        
    end
    
end