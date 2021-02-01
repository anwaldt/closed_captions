files = dir('../RAW/TOS/');

isd = {files.isdir};

fld = {files.folder};

fln = {files.name};


for i=3%:length(files)
    
    if ~isd{i}
        
        disp(['Reading:' fln{i}]);

        subtitle_reader_NETFLIX_TOS([fld{i} '/' fln{i}],5);
        
    end
    
end