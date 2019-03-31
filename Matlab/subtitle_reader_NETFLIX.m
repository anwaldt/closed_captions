SUB = xml2struct('../RAW/Hitchhiker_Netflix.xml');

% SUB = xml2struct('TNG');

% SUB = xml2struct('lost-arc.xml');

% https://www.youtube.com/watch?v=ZpejTczG8Ho

%%

scaleFAC = 70000000;

fid = fopen('test_OUT','w');

XXX= SUB.Children(4).Children(2).Children;


nEntries = length(XXX);

cc = 1;

for entryCNT = 1:nEntries
    
    y = XXX(entryCNT);
    
    T = y.Children;
    
    
    
    if ~isempty(T)
        
        for i=1:length(T)
            
            tt = T(i);
            
            
            if ~isempty(tt.Data)
                
                
                holder  = {y.Attributes.Value};
                
                tStart_SEC  = str2double(holder{1}(1:end-1))/scaleFAC;
                
                
                tStart_MIN =  tStart_SEC/60;
                
                tStart_REM = rem(tStart_MIN,1)*60;
                
                tStart_MIN = floor(tStart_MIN);
                
%                 tStop   = str2double(holder{2}(1:end-1))/60000000 / 60;
                
                tmpLine = tt.Data;
                
                
                if ~isempty(strfind(tmpLine,'(' ))
                     
                    fprintf(fid, num2str(cc));
                    fprintf(fid, '\t\t');
                    
                    fprintf(fid, '%.1f', tStart_SEC);
                    fprintf(fid,'\t');
                    
%                    fprintf(fid, '%3.1f', tStart_REM);
%                    fprintf(fid, '\t\t\t\t');
                    
                    %  fprintf(fid, num2str(tStop));
                    %  fprintf(fid, '\t\t');
                    
                    fprintf(fid, tmpLine);
                    fprintf(fid, '\t');
                    
                    
                    fprintf(fid, '\n');
                    cc = cc+1;
                end
                
                
                
            end
            
        end
        
        
        ff = tt.Children;
        
        
        if ~isempty(ff)
            
            
        end
        
    end
end

fclose(fid);