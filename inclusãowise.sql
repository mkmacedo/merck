//flowtemplatevariable
//abrir em um editor de texto e dar replace em "teste" pela teste que deseja cadastrar o projeto no wise
INSERT INTO wisecapture.flowtemplatevariable (idtenant, flowtemplateid, field, aftertransformfunction, applyorder, automatic, beforetransformfunction, dataformattype, description, enabled, fieldvalidation, keyname, minfuzzyequivalence, partofkey, regexfunction, required, textaliases, textpluck, validationfunction, valuemapentity, valuemapfromfieldname, variableclass) VALUES ('teste', 'unknown', 'tipoDocumento', null, 1, false, null, 'string', '', true, null, 'tipoDocumento', null, true, null, true, {}, null, null, null, null, null);

//flowtemplate
INSERT INTO wisecapture.flowtemplate (idtenant, flowtemplateid, basedsl, businessdoctype, changestatusdsl, creationvalidationdsl, description, documentoriented, documenttypecode, initialstatus, manualnextstepsdsl, ocrtemplatename, type, updatemap) VALUES ('teste', 'not_identified', null, 'NOT_IDENTIFIED', null, 'null', 'Template de fluxo para documento não identificado', true, 'NOT_IDENTIFIED', 'PENDING', 'var result = ""
             if(flowStatus == "PENDING") {
              result = "ON_HOLD,CLOSED,DISCARDED,KLINK_REVIEW,RETURNED,CANCELED,USER_DISCARDED,WAITING,SPAM,DUPLICATED";
             } else if(flowStatus == "ON_HOLD") {
              result = "CLOSED,PENDING,KLINK_REVIEW,SPAM";
             } else if(flowStatus == "CLOSED") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "DISCARDED") {
              result = "PENDING,KLINK_REVIEW";
              } else if(flowStatus == "USER_DISCARDED") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "DONE") {
              result = "ON_HOLD,CLOSED,DISCARDED,KLINK_REVIEW,RETURNED,CANCELED,USER_DISCARDED,WAITING,SPAM";
             } else if(flowStatus == "ERROR") {
              result = "DONE,KLINK_REVIEW,SPAM,ON_HOLD";
             } else if(flowStatus == "RETURNED") {
              result = "PENDING";
              } else if(flowStatus == "WAITING") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "KLINK_REVIEW") {
              result = "ON_HOLD,CLOSED,DISCARDED,PENDING,RETURNED,PENDING,USER_DISCARDED,SPAM,DONE";
             } else if(flowStatus == "PROCESSING") {
              result = "PENDING";
             } else if(flowStatus == "SPAM") {
              result = "ERROR";
             }', 'unknown', 'semiauto', {});
INSERT INTO wisecapture.flowtemplate (idtenant, flowtemplateid, basedsl, businessdoctype, changestatusdsl, creationvalidationdsl, description, documentoriented, documenttypecode, initialstatus, manualnextstepsdsl, ocrtemplatename, type, updatemap) VALUES ('teste', 'unknown', null, 'UNKNOWN', null, null, 'Template de documento desconhecido', true, 'UNKNOWN', 'PROCESSING', 'var result = ""
             if(flowStatus == "PENDING") {
              result = "ON_HOLD,CLOSED,DISCARDED,KLINK_REVIEW,RETURNED,CANCELED,USER_DISCARDED,WAITING,SPAM,DUPLICATED";
             } else if(flowStatus == "ON_HOLD") {
              result = "CLOSED,PENDING,KLINK_REVIEW,SPAM";
             } else if(flowStatus == "CLOSED") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "DISCARDED") {
              result = "PENDING,KLINK_REVIEW";
              } else if(flowStatus == "USER_DISCARDED") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "DONE") {
              result = "ON_HOLD,CLOSED,DISCARDED,KLINK_REVIEW,RETURNED,CANCELED,USER_DISCARDED,WAITING,SPAM";
             } else if(flowStatus == "ERROR") {
              result = "DONE,KLINK_REVIEW,SPAM,ON_HOLD";
             } else if(flowStatus == "RETURNED") {
              result = "PENDING";
              } else if(flowStatus == "WAITING") {
              result = "PENDING,KLINK_REVIEW";
             } else if(flowStatus == "KLINK_REVIEW") {
              result = "ON_HOLD,CLOSED,DISCARDED,PENDING,RETURNED,PENDING,USER_DISCARDED,SPAM,DONE";
             } else if(flowStatus == "PROCESSING") {
              result = "PENDING";
             } else if(flowStatus == "SPAM") {
              result = "ERROR";
             }', 'unknown', 'semiauto', {});

//tasktablecolumn
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'action', null, null, null, 8, true, 'Ações', false);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'flowId', null, null, null, 0, true, 'Id do Fluxo', false);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'keyVariableValue.businessDocType', null, null, null, 2, true, 'Tipo', false);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'keyVariableValue.numeroNota', null, null, null, 3, true, 'Nota', true);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'keyVariableValue.razaoSocialPrestador', null, null, null, 4, true, 'Razão Social', true);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'lastStatusUpdate', 'date', 'yyyy-MM-dd''T''HH:mm:ss.SSSxxxx', 'dd/MM/yyyy HH:mm', 6, true, 'Data Atualização', true);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'name', null, null, null, 1, true, 'Tarefa', true);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'status', null, null, null, 5, true, 'Status', false);
INSERT INTO wisecapture.tasktablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'usersEditingLine', null, null, null, 7, true, 'Usuários Editando', false);

//tasktemplate
INSERT INTO wisecapture.tasktemplate (idtenant, flowtemplateid, tasktemplateid, automatic, delayseconds, description, dsl, formdefinition, formsuccessmessage, initialstatus, mandatory, name, retriesnumber, retriessecondsinterval, routenotification, startaftertaskid, startaftertaskidiffails, statusruledsl, taskorder, tasktype, updatemap) VALUES ('teste', 'unknown', 'emailreader', true, 0, 'Processo de Leitura de Email', null, null, null, 'PENDING', true, 'Leitura de Email', 0, 0, null, null, null, null, 1, 'DOCUMENTUPLOAD', {});
INSERT INTO wisecapture.tasktemplate (idtenant, flowtemplateid, tasktemplateid, automatic, delayseconds, description, dsl, formdefinition, formsuccessmessage, initialstatus, mandatory, name, retriesnumber, retriessecondsinterval, routenotification, startaftertaskid, startaftertaskidiffails, statusruledsl, taskorder, tasktype, updatemap) VALUES ('teste', 'unknown', 'ocr', true, 0, 'Leitura OCR caso necessário', null, null, null, 'PENDING', true, 'OCR do Arquivo', 3, 500, null, 'emailreader', null, null, 2, 'OCR', {});

//wiseuser
INSERT INTO wisecapture.wiseuser (idtenant, username, attribute, email, lastlogin, name, password, randonsalt, recoverpasswordtoken, recoverpasswordtokendue, roles, status) VALUES ('teste', 'fabio.mazzo', 0, 'fabio.mazzo@klink.ai', null, 'Fabio Covolo Mazzo', '$2a$10$NAg.i0c/wyHHi304IzY5f.0wSIpv6ooqgx4AmJ.qcMdOUXKBaGyPy', null, null, null, ['ADMIN', 'USER', 'FLOW'], 'ACTIVE');

//menu
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'Dashboard', 'md-barcode', 'menu.dashboard', 3, null, {'ADMIN', 'FLOW', 'USER'}, false);
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'Flow', 'md-done-all', 'menu.flow', 1, null, {'ADMIN', 'FLOW', 'USER'}, false);
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'Logout', 'md-exit', 'menu.logout', 8, null, {'ADMIN', 'FLOW', 'USER'}, false);
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'TableUpload', 'ios-cloud-upload-outline', 'menu.tableUpload', 5, null, {'ADMIN', 'FLOW', 'USER'}, false);
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'TasksReady', 'ios-briefcase', 'menu.pendingTasks', 2, null, {'ADMIN', 'FLOW', 'USER'}, false);
INSERT INTO wisecapture.menu (idtenant, name, icon, label, "order", parentmenuname, roles, submenu) VALUES ('teste', 'Users', 'md-person', 'menu.users', 1, null, {'ADMIN', 'FLOW', 'USER'}, false);

//tenantconfiguration
INSERT INTO wisecapture.tenantconfiguration (idtenant, analyticstoken, bucketname, defaultdoctype, description, name, prefersecondstorage, secondstorageaccesskey, secondstorageendpoint, secondstorageprovider, secondstoragesecretkey, storageaccesskey, storageendpoint, storageprovider, storageregion, storagesecretkey, useglobalstatusconfig) VALUES ('teste', null, 'teste', 'unknown', 'teste ', 'teste', true, '00240bf6d4ef6040000000001', null, 'backblaze', 'K002OETOpQnPezwwCYredXMnFaIhN4s', 'RP7RACAPSB2RLLWJ82VR', 'https://s3.wasabisys.com', 'Wasabi', null, '14zJ2CSPUuMquP3QjHD3JlWWuGqoYiuaI8RuzYQq', true);

//workflowstatusconfig
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', '**ALL**', null, 'Todos', false, [], 2, 'bg-green-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'CANCELED', null, 'Cancelado', false, [], 8, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'CLOSED', null, 'Fechado', false, [], 5, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'DISCARDED', null, 'Descartado', false, [], 6, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'DONE', null, 'Completo', false, [], 4, 'bg-green-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'DUPLICATED', null, 'Duplicado', false, [], 10, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'ERROR', null, 'Erro', true, [], 3, 'bg-red-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'KLINK_DISCARDED', null, 'Descartado Klink', false, [], 9, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'KLINK_REVIEW', null, 'Revisão Klink', false, [], 9, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'NO_DOCUMENT', null, 'Sem Documento', false, [], 0, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'ON_HOLD', null, 'Análise', false, [], 2, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'PENDING', null, 'Pendente', false, [], 1, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'PROCESSING', null, 'Processando', false, [], 12, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'RETURNED', null, 'Devolvido', false, [], 7, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'SPAM', true, 'Spam', false, [], 15, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'USER_DISCARDED', null, 'Descartado Fiscal', false, [], 6, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'VALIDATED', null, 'Validado', false, [], 7, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'flow', 'WAITING', null, 'Aguardando', false, [], 14, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'DONE', null, 'Completo', false, [], 9, 'bg-green-white');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'ERROR', null, 'Erro', true, [], 10, 'bg-red-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'KLINK_DISCARDED', null, 'Descartado Klink', false, [], 9, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'NOT_APPLICABLE', null, 'Não Aplicável', false, [], 11, 'bg-gray-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'PENDING', null, 'Pendente', false, [], 12, 'bg-yellow-light');
INSERT INTO wisecapture.workflowstatusconfig (idtenant, workflowentity, status, allowmanual, description, indicateserror, manualchangetolist, statusorder, style) VALUES ('teste', 'task', 'READY', null, 'Pronto', false, [], 13, 'bg-green-light');

//flowtablecolumn
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'action', null, null, null, 9, false, 'Ações', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'businessDocType', null, null, null, 1, true, 'Tipo de Documento', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'createdDate', 'date', 'yyyy-MM-dd''T''HH:mm:ss.SS', 'dd/MM/yyyy HH:mm', 4, false, 'Criado em', true);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'id', null, null, null, 0, true, 'id', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'keyVariableValue.numeroNota', null, null, null, 2, true, 'Número da Nota', true);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'keyVariableValue.razaoSocialPrestador', null, null, null, 3, true, 'Razão Social do Prestador', true);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'qtyTasks', null, null, null, 6, false, 'Qtde de Tarefas', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'qtyTasksDone', null, null, null, 7, false, 'Tarefas Concluídas', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'status', null, null, null, 5, true, 'Status', false);
INSERT INTO wisecapture.flowtablecolumn (idtenant, field, columntype, dateinputformat, dateoutputformat, fieldorder, filterable, label, sortable) VALUES ('teste', 'usersEditingLine', 'null', 'null', 'null', 8, false, 'Usuários Editando', false);

//ocrconfiguration
INSERT INTO wisecapture.ocrconfiguration (idtenant, templatename, version, command, description, enabled, enableforceocrconfiguration, enabletable, entityname, generatethumbnails, handlepageasdocument, hidetextlayer, language, mincharstoskipocr, ocrwsendpoint, ocrwslanguage, ocrwslicensecode, ocrwspreprocessing, ocrwsusername, spaceendpoint, spacekey, spacepreprocessing, updatemap, usegooglevisionocr, useocrws, usespace) VALUES ('teste', 'unknown', '1.0', './ocrdocumentofiscalv1.sh //inputFile// //prefix//;', 'OCR otimizado para notas fiscais', true, null, false, 'flow', false, true, 'true', 'por', 400, null, null, null, null, null, null, null, null, {}, true, false, false);