Name:           gcompris
Version:        12.01
Release:        1%{?dist}
Summary:        Educational suite for kids 2-10 years old
Group:          Amusements/Games
License:        GPLv3+
URL:            http://gcompris.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         gcompris-9.0-icon.patch
Buildrequires:  libgnomeui-devel sqlite-devel python-devel gnet2-devel
Buildrequires:  pygtk2-devel SDL_mixer-devel libXt-devel libXxf86vm-devel
Buildrequires:  gnome-python2 xorg-x11-proto-devel gstreamer-devel
Buildrequires:  python-sqlite2 texi2html texinfo
Buildrequires:  perl(XML::Parser) gettext desktop-file-utils gnuchess
BuildRequires:  intltool
BuildRequires:  librsvg2-devel
Requires:       gnuchess gnucap tuxpaint hicolor-icon-theme
Requires:       pygtk2
Requires:       gnome-python2-rsvg
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
# note we do not provide these, they no longer exist
Obsoletes:      %{name}-libs < %{version}-%{release}
# the flags are no longer in a separate sub-package
Obsoletes:      %{name}-flags < %{version}-%{release}
Provides:       %{name}-flags = %{version}-%{release}

%description
GCompris / I Got IT is an educationnal game for children starting at 2.
More than 100 different activities are proposed:
* Click on the animals => learn the mouse/click usage
* Type the falling letters => learn the keyboard usage
* Falling Dices
* Falling words
* Basic algebra
* Time learning with an analog clock
* Puzzle game with famous paintings
* Drive Plane to catch clouds in increasing number
* Balance the scales
* And much more ...

Some activities make use of sounds.  For those you'll have to install the         
gcompris-sound package for the languages you intend to use.


%description -l fr
GCompris / J'ai Compris est un logiciel éducatif pour les enfants 
à partir de 2 ans.

Plus de 100 activités sont proposées :
* Cliquer sur les animaux => apprentissage du click et de la souris
* Entrer les lettres qui tombent => Apprentissage du clavier
* Les dés qui tombent
* Les mots qui tombent
* Algèbre simple
* Apprentissage de la lecture de l'heure sur une horloge analogique
* Puzzle avec des tableaux célèbres
* Pilote un avion pour attraper les nuages dans l'ordre
* Equilibre la balance
* ...


%package sound-ar
Summary:        GCompris voices in Arabic (Tunisia)
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-ar
Voice samples for the GCompris games in Arabic (Tunisia).


%package sound-cs
Summary:        GCompris voices in Tsjech
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-cs
Voice samples for the GCompris games in Tsjech.


%package sound-da
Summary:        GCompris voices in Danish
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-da
Voice samples for the GCompris games in Danish.


%package sound-de
Summary:        GCompris voices in German
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-de
Voice samples for the GCompris games in German.


%package sound-el
Summary:        GCompris voices in Greek
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-el
Voice samples for the GCompris games in Greek.


%package sound-en
Summary:        GCompris voices in English
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-en
Voice samples for the GCompris games in English.


%package sound-es
Summary:        GCompris voices in Spanish
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-es
Voice samples for the GCompris games in Spanish.


%package sound-eu
Summary:        GCompris voices in Basque
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-eu
Voice samples for the GCompris games in Basque.


%package sound-fi
Summary:        GCompris voices in Finish
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-fi
Voice samples for the GCompris games in Finish.


%package sound-fr
Summary:        GCompris voices in French
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-fr
Voice samples for the GCompris games in French.


%package sound-hi
Summary:        GCompris voices in Hindi
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-hi
Voice samples for the GCompris games in Hindi.


%package sound-hu
Summary:        GCompris voices in Hungarian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-hu
Voice samples for the GCompris games in Hungarian.


%package sound-id
Summary:        GCompris voices in Indonesian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-id
Voice samples for the GCompris games in Indonesian.


%package sound-it
Summary:        GCompris voices in Italian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-it
Voice samples for the GCompris games in Italian.


%package sound-mr
Summary:        GCompris voices in Indian Marathi
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-mr
Voice samples for the GCompris games in Indian Marathi.


%package sound-nb
Summary:        GCompris voices in Norwegian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-nb
Voice samples for the GCompris games in Norwegian.


%package sound-nl
Summary:        GCompris voices in Dutch
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-nl
Voice samples for the GCompris games in Dutch.


%package sound-pt
Summary:        GCompris voices in Portuguese
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-pt
Voice samples for the GCompris games in Portuguese.


%package sound-ru
Summary:        GCompris voices in Russian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-ru
Voice samples for the GCompris games in Russian.


%package sound-so
Summary:        GCompris voices in Somali
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-so
Voice samples for the GCompris games in Somali.


%package sound-sr
Summary:        GCompris voices in Serbian
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-sr
Voice samples for the GCompris games in Serbian.


%package sound-sv
Summary:        GCompris voices in Swedish
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-sv
Voice samples for the GCompris games in Swedish.


%package sound-tr
Summary:        GCompris voices in Turk
Group:          Amusements/Games
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description sound-tr
Voice samples for the GCompris games in Turk.


%prep
%setup -q
%patch0 -p1
for file in docs/C/%{name}.info AUTHORS ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build
export CFLAGS="$RPM_OPT_FLAGS `pkg-config --cflags pangoft2`"
# The configure check for python-gnome.canvas fails without X running,
# --enable-py-build-only works around this
%configure --enable-py-build-only --enable-gnet
# we can't use %%{?_smp_mflags} because that breaks compilation!
make 
# Fixup the desktop files a bit, we don't use a patch in %%prep because that
# breaks the translations
sed -i \
  -e 's/Name=Educational suite GCompris/Name=GCompris Educational suite/' \
  -e 's/Categories=Game;KidsGame;/Categories=Education;/' \
  %{name}.desktop
sed -i \
  -e 's/Comment=Administration for gcompris/Comment=Specify which activities may be used by whom/' \
  -e 's/Categories=Education;Teaching;/Categories=Education;/' \
  %{name}-edit.desktop


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -fr $RPM_BUILD_ROOT/usr/lib/menu
%find_lang %{name}

# below is the desktop file and icon stuff.
desktop-file-install --vendor fedora --delete-original                  \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor fedora --delete-original                  \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-edit.desktop

#remove not needeed ".desktop" file (use for windows build)
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/nsis_translations.desktop
#remove not needed libgoocanvas devel so symlink
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libgoocanvas.so

mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
mv $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}.png \
  $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}-edit.png \
  $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps
rmdir $RPM_BUILD_ROOT/usr/share/pixmaps


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}
%exclude %{_datadir}/%{name}/boards/voices
%{_datadir}/icons/hicolor/48x48/apps/%{name}*.png
%{_datadir}/applications/fedora-%{name}*.desktop
%{_infodir}/%{name}.info.gz
%{_mandir}/man6/%{name}.6.gz

%files sound-ar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/ar

%files sound-cs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/cs

%files sound-da
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/da

%files sound-de
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/de

%files sound-el
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/el

%files sound-en
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/en

%files sound-es
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/es

%files sound-eu
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/eu

%files sound-fi
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/fi

%files sound-fr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/fr

%files sound-hi
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/hi

%files sound-hu
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/hu

%files sound-id
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/id

%files sound-it
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/it

%files sound-mr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/mr

%files sound-nb
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/nb

%files sound-nl
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/nl

%files sound-pt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/pt
%{_datadir}/%{name}/boards/voices/pt_BR

%files sound-ru
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/ru

%files sound-so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/so

%files sound-sr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/sr

%files sound-sv
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/sv

%files sound-tr
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/boards
%dir %{_datadir}/%{name}/boards/voices
%{_datadir}/%{name}/boards/voices/tr


%changelog
* Sat Jan 14 2012 Hans de Goede <hdegoede@redhat.com> - 12.01-1
- New upstream release 12.01 (rhbz#781359)
- Drop our patches (all upstreamed)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Hans de Goede <hdegoede@redhat.com> - 11.12-1
- New upstream release 11.12
- Drop our patches (all upstreamed)

* Wed Dec 07 2011 Hans de Goede <hdegoede@redhat.com> - 11.09-1
- New upstream release 11.09

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 9.5-5
- Rebuild for new libpng

* Wed Feb  9 2011 Hans de Goede <hdegoede@redhat.com> - 9.5-4
- Fix building with gcc 4.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  1 2011 Hans de Goede <hdegoede@redhat.com> - 9.5-2
- Remove bogus -devel subpackage (rhbz#566359)

* Mon Dec 06 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.5-1
- 9.5

* Sat Jul 31 2010 Johan Cwiklinski <johan AT x-tnd DOT be> - 9.3-3
- Fix GTK build error

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 27 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.3-1
- 9.3

* Sun Feb 14 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.2-2
- 9.2-2

* Sat Feb 13 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.2-1
- 9.2

* Fri Feb 12 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.1-2
- Fix DSO link bug

* Mon Jan 25 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.1-1
- 9.1

* Sun Jan 17 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.0-5
- Fix for deprecated gtk functions

* Sun Jan 17 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.0-4
- Remove python-sqlite2 requires (part of python since 2.5, bug #480426)
- Fix overlaping dice in smallnumber activity

* Fri Jan 08 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.0-3
- Patch for photohunter in fullscreen (from upstream)

* Thu Jan 07 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.0-2
- Added missing gnome-python2-rsvg requires

* Mon Jan 04 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 9.0-1
- New GCompris 9.0

* Sat Oct 24 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.13-1
- New upstream bugfix release 8.4.13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 29 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.12-1
- New upstream bugfix release 8.4.12

* Thu Mar 12 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.11-1
- New upstream bugfix release 8.4.11

* Mon Mar 9 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.9-1
- New wupstream bugfix release 8.4.9

* Fri Feb 27 2009 Johan Cwiklinski <johan AT x-tnd DOT be> - 8.4.8-4
- Fix python 2.6 reserved keyword

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 8.4.8-2
- Rebuild for Python 2.6

* Tue Oct 7 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.8-1
- New upstream bugfix release 8.4.8

* Tue Oct 7 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.7-1
- New upstream bugfix release 8.4.7

* Fri Aug 8 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.6-1
- New upstream bugfix release 8.4.6

* Thu May 29 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4.5-2
- Fix gcompris not starting anymore (oops) (bz 448642)

* Thu May 15 2008 Johan Cwiklinski <johan AT x-tnd DOT be> 8.4.5-1
- New upstream bugfix release 8.4.5

* Wed Feb 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4.4-1
- New upstream bugfix release 8.4.4

* Wed Oct 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4.2-1
- New upstream bugfix release 8.4.2

* Fri Oct 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4.1-1
- New upstream bugfix release 8.4.1
- Drop integrated patches

* Sat Sep 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4-2
- Fix keyboard not working in fullscreen mode

* Tue Sep 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.4-1
- New upstream release 8.4
- Drop -flags sub-package, the idea was that by putting the flags in a
  subpackage they could be used by other packages, but this never happened.
- License changed to GPL version 3 (or higher)

* Thu Aug 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.3.3-1
- New upstream release 8.3.3

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.3.2-3
- Update License tag for new Licensing Guidelines compliance

* Mon Jul 16 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.3.2-2
- Rebase to upstream 8.3.2-2 tarbal "respin" <grrr>
- Add a patch to stop unnecessary monitor resolution switching when starting
  tuxpaint in fullscreen mode.

* Tue Jun 19 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.3.2-1
- New upstream release 8.3.2
- Drop upstreamed patches

* Sat May 26 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 8.3.1-1
- New upstream release 8.3.1
- Upstream no longer has parts of its code in a library, so the drop the
  -libs and -devel subpackages

* Fri Dec 22 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 8.2.2-2
- Update src/boards/canvas.c to canvas.c from latest gnome-python2 to
  fix build with python 2.5

* Wed Dec 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 8.2.2-1
- New upstream release 8.2.2-2

* Fri Dec 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 8.2-2
- Rebuid for python 2.5 (blind (untested) rebuild as I cannot upgrade
  to python 2.5 since plague hasn't been rebuild yet).

* Tue Nov  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 8.2-1
- New upstream release 8.2
- Drop most patches (integrated upstream)
- Drop seperate / addon man page (integrated upstream)

* Sun Oct 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 8.1-1
- New upstream release 8.1
- Drop most patches (integrated upstream)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-14
- FE6 Rebuild

* Sun Aug 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-13
- Fix BZ 197758 (backport from upstream CVS)

* Mon Jul  3 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-12
- Restore the original resolution and ungrab the mouse on focus out, redo
  on focus in. This allows alt-tab-ing away when in fullscreen mode. And
  more importantly makes gnome-screensaver happy when trying to run while
  gcompris is running in fullscreen mode (BZ 197276).

* Mon Jun  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-11
- Various improvments to the new fullscreen code.

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-10
- Add a hard Requires on gcompris-libs version-release to the base package
  because upstream doesn't bump the soname version when the abi changes.
- Fix 2 more bugs introduced by the fix for bug 190918 (sigh, sorry).

* Tue May  9 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-9
- Fix 2 bugs introduced by the fix for bug 190918, see the bug for details.

* Sun May  7 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-8
- Change Xrandr BR to Xxf86vm BR.

* Sat May  6 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-7
- Use XF86VidMode instead of Xrandr extension for resolution switching,
  hopefully fixing bug 190918.

* Fri May  5 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-6
- Add missing python module Requires.

* Mon May  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-5
- Make -devel require -libs instead of -lib (oops).

* Sat Apr 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-4
- Add click_on_letter.patch from CVS which fixes a few problems with the
  click on letter activity when the sounds are not installed

* Thu Apr 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-3
- Don't use a patch on the .desktop files as that breaks the translations,
  instead use sed at the end of %%build

* Tue Apr 25 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-2
- Fix a few parser errors in nl.po
- Drop Patch0, instead use a configure option with the same effect

* Mon Apr 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 7.4-1
- Initial spec file
