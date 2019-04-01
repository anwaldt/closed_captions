



function [] = subtitle_reader_NETFLIX_TNG(inFile, scaleFAC, outFile)


if nargin<3
    
    [~,y,~] = fileparts(inFile);
    outFile = [y '.sub'];
end

if nargin<2
    scaleFAC = 41000000;
end

SUB = xml2struct(inFile);

%%


fid = fopen(outFile,'w');

XXX= SUB.Children(4).Children(2).Children;


nEntries = length(XXX);

cc = 1;

%%

for entryCNT = 1:nEntries
    
    y = XXX(entryCNT);
    
    T = y.Children;
    
    
    
    if ~isempty(T)
        
        for i=1:length(T)
            
            tt = T(i);
            
            
            if ~isempty(tt.Data)
                
                
                
                tmpID = tt.Data;
                
                
                if ~isempty(strfind(tmpID,'(' ))
                    
                    
                    
                    
                    holder  = {y.Attributes.Value};
                    
                    tStart_SEC  = str2double(holder{1}(1:end-1))/scaleFAC;
                    
                                
                    tStop_SEC  = str2double(holder{2}(1:end-1))/scaleFAC;

                     
                    
                    
                    tmpLine = T(2).Children.Data;
                    
                    fprintf(fid, num2str(cc));
                    fprintf(fid, '\t\t');
                    
                    fprintf(fid, '%.1f', tStart_SEC);
                    fprintf(fid,'\t');
%                      
%                     fprintf(fid, '%.1f', tStop_SEC);
%                     fprintf(fid,'\t');
                    
                    
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