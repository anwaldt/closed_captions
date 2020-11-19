files = dir('/home/anwaldt/Desktop/closed_captions/RAW/TNG/');

isd = {files.isdir};

fld = {files.folder};

fln = {files.name};


for i=1:length(files)
    
    if ~isd{i}

        subtitle_reader_NETFLIX_TNG([fld{i} '/' fln{i}],2)
        
    end
    
end