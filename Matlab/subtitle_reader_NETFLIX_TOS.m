



function [] = subtitle_reader_NETFLIX_TOS(inFile, scaleFAC, outFile)


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



fprintf(fid, num2str(0));
fprintf(fid, '\t\t');

fprintf(fid, '%.1f', 0);
fprintf(fid,'\t');

fprintf(fid, '---');
fprintf(fid, '\t');

fprintf(fid, '\n');


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
                
                if ~isempty(strfind(tmpID,'[' )) || ~isempty(strfind(tmpID,'(' ))
                                        
                    tStart_SEC  = (str2double(y.Attributes(1).Value(1:end-1))) / scaleFAC;
                    
                    tStop_SEC  = (str2double(y.Attributes(2).Value(1:end-1))) /scaleFAC ;
                    
                    % keep original lenth
                    % tStop_SEC = tStart_SEC + (tStop_SEC - tStart_SEC) * scaleFAC;
                    
                    
                    % This is an alternate veriosn
                    tmpLine = T(1).Data;
                    if length(tmpLine)>1
                        
                        outLine = tmpLine; % T.Data(2:end-2);
                  
                        
                        fprintf(fid, num2str(cc));
                        fprintf(fid, '\t\t');
                        
                        fprintf(fid, '%.1f', tStart_SEC);
                        fprintf(fid,'\t');
                        
                        fprintf(fid, outLine);
                        fprintf(fid, '\t');
                        
                        fprintf(fid, '\n');
                        
                        
                        fprintf(fid, num2str(0));
                        fprintf(fid, '\t\t');
                        
                        fprintf(fid, '%.1f', tStop_SEC);
                        fprintf(fid,'\t');
                        
                        fprintf(fid, '---');
                        fprintf(fid, '\t');
                        
                        fprintf(fid, '\n');
                        
                        
                        cc = cc+1;
                    end
                end
                
            end
            
        end
        
        ff = tt.Children;
        
        if ~isempty(ff)
            
        end
        
    end
end

fclose(fid);